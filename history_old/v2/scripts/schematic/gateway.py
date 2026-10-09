"""Execute reviewed JavaScript through the official local EasyEDA bridge.

Never retry mutations automatically: a timeout may follow a successful edit.
"""
import argparse
import json
import urllib.request
import urllib.error
from pathlib import Path


def request(path, payload=None, port=49620):
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(f"http://127.0.0.1:{port}/{path}", data=data,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(error.read().decode('utf-8', errors='replace')) from error


def execute(code, port=49620, project_name='SonoField-FPGA-v2-Schematic-V1'):
    health = request("health", port=port)
    if health.get("service") != "easyeda-bridge" or not health.get("edaConnected"):
        raise RuntimeError("Official bridge or EDA connection unavailable")
    windows = request("eda-windows", port=port)
    if windows.get("count") != 1:
        raise RuntimeError("Expected one EDA window; select explicitly before continuing")
    if project_name not in ['SonoField-FPGA-v2-Schematic-V1', 'SonoField-FPGA-v2-Schematic-V1-SingleSheet']:
        raise ValueError('Unapproved project identity')
    guard = "const project=await eda.dmt_Project.getCurrentProjectInfo();if(project?.friendlyName!=="+json.dumps(project_name)+")throw new Error('Wrong project');"
    result = request("execute", {"code": guard + code,
                                  "windowId": windows["activeWindowId"]}, port)
    if not result.get("success"):
        raise RuntimeError(json.dumps(result))
    return result["result"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument('--project', default='SonoField-FPGA-v2-Schematic-V1')
    args = parser.parse_args()
    result = execute(args.script.read_text(encoding="utf-8-sig"),project_name=args.project)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved verified API response: {args.output}")
