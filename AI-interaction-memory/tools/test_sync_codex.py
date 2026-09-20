"""Privacy and provenance tests; synthetic fixtures contain no real credentials."""
import json
from pathlib import Path
import tempfile
import unittest
import sync_codex as sync


class CaptureTests(unittest.TestCase):
    def setUp(self):
        scratch = sync.REPO / "build" / "interaction_tests"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.source = self.repo / "rollout.jsonl"

    def fixture(self, extra=()):
        rows = [{"type": "session_meta", "payload": {"id": "test-thread", "cwd": str(self.repo), "timestamp": "2026-09-20T00:00:00Z"}}]
        for role, phase, text in [("user", None, "原始用户指令\r\n第二行"), ("assistant", "commentary", "实际进展"),
                                  ("assistant", "final_answer", "实际结果"), ("assistant", None, "HIDDEN_SENTINEL"),
                                  ("developer", None, "PRIVATE_INSTRUCTIONS")]:
            rows.append({"type": "response_item", "timestamp": "2026-09-20T00:00:01Z", "payload": {
                "type": "message", "role": role, "phase": phase,
                "content": [{"type": "input_text" if role == "user" else "output_text", "text": text}]}})
        rows.extend(extra)
        self.source.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")

    def test_visible_allowlist_and_utf8(self):
        self.fixture([{"type": "response_item", "payload": {"type": "reasoning", "text": "REASON_SENTINEL"}},
                      {"type": "compacted", "payload": {"summary": "SUMMARY_SENTINEL"}}])
        m = sync.export(self.source, self.repo)
        text = (self.repo / "AI-interaction-memory/codex/test-thread.md").read_text(encoding="utf-8")
        self.assertEqual(m["message_count"], 3)
        self.assertIn("原始用户指令", text)
        for secret in ("HIDDEN_SENTINEL", "PRIVATE_INSTRUCTIONS", "REASON_SENTINEL", "SUMMARY_SENTINEL"):
            self.assertNotIn(secret, text)
        self.assertEqual(m["sync_status"], "PARTIAL")

    def test_secret_redaction_and_idempotence(self):
        token = "ghp_" + "X" * 36
        original = token + " password=synthetic_fixture_123 Bearer " + "Z" * 30 + " person@example.test C:\\Users\\person\\file"
        clean = sync.sanitize(original)
        self.assertNotIn(token, clean)
        self.assertNotIn("synthetic_fixture_123", clean)
        self.assertNotIn("person@example.test", clean)
        self.assertNotIn("Users\\person", clean)
        self.assertEqual(sync.sanitize(clean), clean)

    def test_repeat_and_append(self):
        self.fixture()
        first = sync.export(self.source, self.repo)
        transcript = self.repo / "AI-interaction-memory/codex/test-thread.md"
        modified = transcript.stat().st_mtime_ns
        self.assertEqual(first, sync.export(self.source, self.repo))
        self.assertEqual(transcript.stat().st_mtime_ns, modified)
        with self.source.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "新增"}]}}) + "\n")
        self.assertEqual(sync.export(self.source, self.repo)["message_count"], 4)
        self.assertEqual(sync.check(self.repo)["status"], "PASS")

    def test_wrong_workspace_rejected(self):
        self.fixture()
        with self.assertRaisesRegex(ValueError, "workspace"):
            sync.extract(self.source, self.repo / "different")

    def test_changed_history_rejected(self):
        self.fixture(); sync.export(self.source, self.repo)
        text = self.source.read_text(encoding="utf-8").replace("原始用户指令", "changed")
        self.source.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "lost/changed"):
            sync.export(self.source, self.repo)

    def test_tampered_export_rejected(self):
        self.fixture(); sync.export(self.source, self.repo)
        path = self.repo / "AI-interaction-memory/codex/test-thread.md"
        with path.open("a", encoding="utf-8") as f:f.write("tampered")
        with self.assertRaisesRegex(ValueError, "integrity"):
            sync.check(self.repo)

    def test_tool_payloads_never_copied(self):
        self.fixture([{"type": "response_item", "payload": {"type": "custom_tool_call", "call_id": "call-1", "name": "functions.exec", "input": "INPUT_SENTINEL"}},
                      {"type": "response_item", "payload": {"type": "custom_tool_call_output", "call_id": "call-1", "output": "OUTPUT_SENTINEL"}}])
        sync.export(self.source, self.repo)
        text = (self.repo / "AI-interaction-memory/tool-flow/test-thread.md").read_text(encoding="utf-8")
        self.assertIn("call-1", text)
        self.assertNotIn("INPUT_SENTINEL", text)
        self.assertNotIn("OUTPUT_SENTINEL", text)

    def test_incomplete_tail(self):
        self.fixture()
        with self.source.open("ab") as f:f.write(b'{"unfinished":')
        self.assertTrue(sync.export(self.source, self.repo)["incomplete_tail"])


if __name__ == "__main__":unittest.main()
