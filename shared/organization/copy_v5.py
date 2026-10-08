"""User-authorized selective copy. Old sources stay byte-identical; no overwrites."""
from pathlib import Path
import json, shutil, subprocess, hashlib

REPO=Path(__file__).resolve().parents[2]; SRC=REPO/'v2'; DST=REPO/'v5'
SCRIPTS={'validate.py','check_waveform.py','self_calibration_gate.py','board_transport_gate.py','generate_system.py','generate_transport.py',
    'timing_equivalence.py','pre_pcb_checks.py','check_repository.py','check_migration.py','ps_platform_preflight.py','run_motion_app.ps1','create_project.tcl','audit_bom.py','motion_gate.py'}
CONFIGS={'acoustic_baseline.json','system_baseline.json','register_map.json','transport_protocol.json','motion_profile.json','hardware_parts.json','board_transport_profile.json','board_smoke_profile.json'}
DOCS={'architecture/SELF_CALIBRATION.md','architecture/REGISTER_MAP.md','architecture/digital_interface.md','architecture/V2_REQUIREMENTS.md',
      'theory/model_and_results.md','hardware/PCB_SOFTWARE_INTERFACE.md','hardware/PCB_SOFTWARE_INTERFACE_REQUIREMENTS.md',
      'hardware/SERIALIZER_THROUGHPUT_PROOF.md','hardware/SCHEMATIC_DESIGN_RULES.md','hardware/tct40_baseline.md','experiments/bringup.md','dependencies.md','RESEARCH_BASELINE.md'}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,t):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t,encoding='utf-8',newline='\n')

if __name__=='__main__':
    tracked=[p for p in subprocess.check_output(['git','ls-files','-z','v2'],cwd=REPO).decode('utf-8').split('\0') if p]
    inventory=[]
    for name in tracked:
        rel=Path(name).relative_to('v2').as_posix(); dest=None
        if rel.startswith(('rtl/','software/','tb/','tests/','firmware/','hardware/bom/','hardware/characterization/','hardware/mechanical/','hardware/transducers/user_supplied/')) or rel.startswith('requirements') or rel=='hardware/transducers/10mm_supplier_reference.md':dest=rel
        elif rel.startswith('scripts/') and Path(rel).name in SCRIPTS and len(Path(rel).parts)==2:dest=rel
        elif rel.startswith('config/') and Path(rel).name in CONFIGS:dest=rel
        elif rel.startswith('docs/motion/') or (rel.startswith('docs/') and rel[5:] in DOCS):dest=rel.replace('V2_REQUIREMENTS','V5_REQUIREMENTS')
        elif rel=='evidence/self_calibration_stage/validation_frequency/self_calibration/calibration.json':dest='simulation/fixtures/calibration_reference.json'
        elif rel=='evidence/pre_pcb_board_ready/timing/baseline/motion_queue.sv':dest='simulation/golden/motion_queue.sv'
        elif rel=='evidence/pre_pcb_board_ready/timing/baseline/calibration_scheduler.sv':dest='simulation/golden/calibration_scheduler.sv'
        elif rel=='evidence/core_timing_real_loop/baseline/burst_generator.sv':dest='simulation/golden/burst_generator.sv'
        item={'source':name,'target':'v5/'+dest if dest else None,'classification':'COPY_AS_IS' if dest else 'DO_NOT_COPY',
              'reason':'Reusable current core/interface/test or reference input' if dest else 'Historical evidence,old board pin/config,old reproduction or EDA authoring script excluded',
              'source_sha256_bytes':sha(REPO/name)}
        inventory.append(item)
    plan=REPO/'shared/organization/VERSION_MIGRATION_PLAN.md'
    write(plan,'# v5 reuse inventory\n\nDirect user approves v5 AX7020; source currentv2 with core validated at9936a737. v4 is not created. Old versions kept intact. Complete per-file classifications: VERSION_MIGRATION_PLAN.json.\n\n'
        'COPY_AS_IS: RTL/TB/tests/firmware,algorithms,geometry,transducer/BOM reference. COPY_AND_UPDATE: copied orchestration paths/version labels/board gates and current docs. REGENERATE: all evidence/build/cache/current board config. DO_NOT_COPY: Robei boardfacts/identity/DDR/pins/J3-J6 budgets,XDC,old native EDA scripts,old evidence/PASS reports,old model-specific management generators. UNKNOWN: user current AX7020 board revision,PS/XSA/connector allocation; stop physical deployment until sourced.\n\n'
        'BOM/reference circuits remain unqualified inherited design input; they are not AX7020 electrical release. Golden RTL fixtures are explicit historical validation inputs copied into v5/simulation/golden, not hidden loads from old evidence. Normal v5 operation must not open old-version source.\n')
    (plan.with_suffix('.json')).write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    # Plan and all target collisions verified before the first engineering copy.
    for item in inventory:
        if item['target'] and (REPO/item['target']).exists():raise RuntimeError('Refuse overwrite '+item['target'])
    for item in inventory:
        if item['target']:
            out=REPO/item['target'];out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(REPO/item['source'],out)
            assert sha(out)==item['source_sha256_bytes']
    for folder in ['hardware/ax7020','hardware/constraints','hardware/pcb','vivado','evidence','simulation','docs','config']:(DST/folder).mkdir(parents=True,exist_ok=True)
    items=[i for i in inventory if i['target']]
    (DST/'config/inheritance_manifest.json').write_text(json.dumps({'source_version':'v2','source_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO).decode().strip(),
      'source_validated_core_commit':'9936a737c45bf61f1908863a94f6374c6b5c828c','files':items},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'copied_files':len(items),'excluded_files':len(inventory)-len(items),'old_versions_modified':False}))
