from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
class TestContributors(unittest.TestCase):
    def test_contributor_files(self):
        for f in (ROOT/'contributors').glob('*.md'):
            if f.name.startswith('_'): continue
            text=f.read_text(encoding='utf-8').strip()
            self.assertTrue(text.startswith('# Display name:'), f'{f.name}: missing name line')
            self.assertIn('City (optional):',text, f'{f.name}: missing city field')
            self.assertIn('I want to build with AI:',text, f'{f.name}: missing AI project field')
            self.assertNotIn('YOUR_',text, f'{f.name}: replace placeholders')
            self.assertNotRegex(text, r'(?i)(sk-[A-Za-z0-9]{16,}|password\s*[:=])')
