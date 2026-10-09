"""Fail on hidden legacy runtime paths, foreign source files or missing v5 assets."""
from pathlib import Path
import json,re,ast

ROOT=Path(__file__).resolve().parents[1]
def audit():
    errors=[];scanned=[]
    for folder in ('rtl','software','scripts','tests','tb','firmware'):
        for p in (ROOT/folder).rglob('*'):
            if p.suffix not in ('.py','.ps1','.tcl','.sv','.svh','.c','.h'):continue
            text=p.read_text(encoding='utf-8');scanned.append(p.relative_to(ROOT).as_posix())
            if p.suffix=='.py':ast.parse(text,filename=str(p))
            normalized=text.replace('\\','/')
            if p.name!='check_structure.py' and re.search(r'(?<![\w])(?:v[123]/|Zynq7020/|archive/|parameter[-_]detection/)',normalized):
                errors.append('Legacy runtime path '+str(p.relative_to(ROOT)))
            if re.search(r'(?i)[EG]:[/\\]Codex[-_]project',text):errors.append('Hard-coded workspace '+str(p.relative_to(ROOT)))
    for rel in ('config/board_facts.json','config/board_smoke_profile.json','config/system_baseline.json',
                'rtl/sono_axi_system.sv','hardware/constraints/core_ooc.xdc','simulation/golden/motion_queue.sv'):
        if not (ROOT/rel).is_file():errors.append('Missing '+rel)
    facts=json.loads((ROOT/'config/board_facts.json').read_text(encoding='utf-8'))
    if facts['board']!='ALINX AX7020' or facts['physical_part'] is not None or facts['production_xdc'] is not None:
        errors.append('Unverified hardware configuration promoted')
    return {'status':'FAIL' if errors else 'PASS','errors':errors,'scanned_files':len(scanned),
            'old_version_source_dependency':False if not errors else 'REVIEW_REQUIRED','board_deployment':'BLOCKED_BY_REVISION_PS_AND_IO_QUALIFICATION'}

if __name__=='__main__':
    r=audit();print(json.dumps(r,indent=2));raise SystemExit(bool(r['errors']))
