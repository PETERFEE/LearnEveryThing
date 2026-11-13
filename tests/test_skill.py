"""Standard-library smoke tests for resource selection and skill validation."""
import importlib.util
from pathlib import Path
import json
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import roadmap
import validate_catalog

class TestSkill(unittest.TestCase):
    def test_validated(self):
        self.assertEqual(validate_catalog.validate(),[])
    def test_count_unique(self):
        r=roadmap.load_catalog()
        self.assertEqual(len(r),146)
        self.assertEqual(len(set(x['id'] for x in r)),146)
    def test_learner_select(self):
        p=json.loads((ROOT/'assets'/'learner_profile.example.json').read_text())
        selected=roadmap.pick_resources(p,12)
        self.assertEqual(len(selected),12)
        self.assertNotIn(4,{x['tier'] for x in selected})
        self.assertIn('D',{x['domain_id'] for x in selected})
        out=roadmap.markdown(p,selected)
        self.assertIn('Weeks',out)
        self.assertIn('Capstone',out)
        self.assertIn('offline',out)
    def test_standalone_firmware_excludes_ros(self):
        p={'target_roles':['embedded-firmware'],'learning_gaps':['rtos','testing'],'known_skills':['c']}
        sel=roadmap.pick_resources(p,10)
        self.assertEqual(len(sel),10)
        self.assertFalse(any(x['domain_id']=='D' for x in sel))

if __name__=='__main__':unittest.main()
