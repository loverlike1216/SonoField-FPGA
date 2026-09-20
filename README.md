# SonoField-FPGA · v1

PROJECT_ID: SONOFIELD_FPGA. Repository: https://github.com/loverlike1216/SonoField-FPGA.
当前唯一版本为 **v1**，分支 main。本次整理目录和协作记录，不升级版本。

上下各 8×8，10 mm 名义换能器，辐射面中心点距 12 mm；面间距默认 100 mm，可调 90–115 mm。
原点为全部辐射面中心的几何中心，默认 Z=±50 mm。尚无实物悬浮结果。

| 路径 | 用途 |
|---|---|
| [v1/](v1/README.md) | 当前完整工程：RTL、模型、测试、脚本、硬件资料、技术文档及证据 |
| [shared/](shared/PROJECT_STATE.md) | 当前状态、版本门禁、决策、阻塞、计划与交接 |
| [AI-chat-memory/](AI-chat-memory/INDEX.md) | 指定 ChatGPT 对话的来源与真实同步状态 |
| [AI-interaction-memory/](AI-interaction-memory/INDEX.md) | Codex 原始可见消息、会话索引、工具流与同步命令 |
| [AI-problem/](AI-problem/README.md) | 带证据的问题与待取得的外部决策 |
| [CHANGELOG.md](CHANGELOG.md) | 当前工程变更记录 |
| Zynq7020/ | 用户本地板卡原始资料，位置不变，不发布 |
| .venv/、build/ | Git 忽略的公共环境、缓存和复现工作目录 |

## 运行

从仓库根目录使用 PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r v1/requirements-lock.txt
Set-Location v1
..\.venv\Scripts\python.exe -m unittest discover -s tests -v
..\.venv\Scripts\python.exe scripts/validate.py --output build/verification_review
..\.venv\Scripts\python.exe -m software.acoustic_model.export_geometry --output build/geometry_review
..\.venv\Scripts\python.exe scripts/check_repository.py
```

详见 [操作指南](v1/docs/OPERATING_GUIDE.md)、[坐标定义](v1/hardware/mechanical/radiating_surface_geometry.md)、
[交接](shared/HANDOFF.md)和[验收](shared/ACCEPTANCE.md)。
需要 Python 3.10、Icarus、Vivado 2025.2；锁定依赖在 v1 内。

当前 Chat Source 为 SonoField-FPGA；未发现可读取该 ChatGPT 历史的工具，同步状态 BLOCKED。
这不阻止当前目录整理。板卡完整料号、IO 电压及换能器电气表征仍有独立硬件阻塞。
历史提交保留在 Git，当前树只维护 v1；不得把数字验证通过写成综合或实物通过。
