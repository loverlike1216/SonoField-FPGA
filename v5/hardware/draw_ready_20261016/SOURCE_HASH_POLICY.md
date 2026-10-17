# Source hash policy

FINAL_NATIVE_SOURCE_RAW_SHA256.json preserves exact Windows input bytes captured before native21. FINAL_NATIVE_SOURCE_MANIFEST.json uses SHA256 after CRLF→LF normalization so Git LF checkout can reproduce the same source content. No other character, whitespace, RTL logic or constraint normalization is performed. Original frozen_parent gate and its hashes are unchanged and still FAIL for authorized source edits; this new manifest does not override that gate.

The public delivery packet has a local .gitattributes which disables text conversion for packet files. DELIVERY_SHA256.csv therefore records exact packet bytes, including original report formatting and UTF-8 BOM CSVs. The manifest excludes itself and the later publication receipt. This packet rule does not change formal RTL source attributes or the canonical native-source hash policy above.
