> v5 inherited design/reference documentation. Original source is recorded in config/inheritance_manifest.json. Technical behavior/requirements are retained; historical numeric results are reference inputs, not v5 validation or AX7020 electrical qualification. Current board facts are config/board_facts.json; baseline results are evidence/BASELINE_VALIDATION.md.

# PCB software interface requirements

The complete current contract is [PCB_SOFTWARE_INTERFACE.md](PCB_SOFTWARE_INTERFACE.md).
This named handoff entry implements section 60 of the formal user instruction without duplicating
the register, voltage, sample-format and timing specification. Treat that linked document together
with config/system_baseline.json, config/hardware_parts.json and config/register_map.json as the
review set. No connector pin assignment, schematic, fabrication or physical validation is implied.
