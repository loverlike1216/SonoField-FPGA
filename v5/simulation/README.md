# Explicit validation inputs

Golden RTL files retain exact historical behavior for independent equivalence checks. fixtures/calibration_reference.json is copied from a historical SYNTHETIC test record with original content and v2 metadata intact; it is not board characterization, calibration evidence or a current hardware record. v5 UI and motion unit tests now read this explicit local fixture. All source paths/hashes are recorded in config/inheritance_manifest.json. Current generated evidence never silently becomes an input fixture.
