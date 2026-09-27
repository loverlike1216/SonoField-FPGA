"""Regression for the two real problem-digest formats already present in this repo."""
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_repository import verify_problem


class ProblemIntegrityTests(unittest.TestCase):
    def test_body_hash_detects_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'P-test.md';body='\nOriginal engineering evidence\n'
            text='---\nproblem_id: P-test\nproblem_hash: '+hashlib.sha256(body.encode()).hexdigest()+'\n---\n'+body
            p.write_text(text,encoding='utf-8');self.assertTrue(verify_problem(p)[1])
            p.write_text(text+'tampered\n',encoding='utf-8');self.assertFalse(verify_problem(p)[1])

    def test_adjacent_hash_detects_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'P-test.md';text='---\nproblem_id: P-test\nproblem_hash: SEE_ADJACENT_SHA256_FILE\n---\nOriginal\n'
            p.write_text(text,encoding='utf-8');p.with_suffix('.sha256').write_text(hashlib.sha256(text.encode()).hexdigest()+'  '+p.name+'\n')
            self.assertTrue(verify_problem(p)[1])
            p.write_text(text+'tampered\n',encoding='utf-8');self.assertFalse(verify_problem(p)[1])
            p.with_suffix('.sha256').write_text('0'*64+'  ../other.md\n')
            with self.assertRaises(ValueError):verify_problem(p)


if __name__=='__main__':unittest.main()
