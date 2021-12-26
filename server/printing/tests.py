from django.test import TestCase

import re


from .controllers import *

# Create your tests here.
class ControllerTest(TestCase):
    def test_clear_file_name:
        clear_file_name('')
        self.assertEqual(len(
            clean_file_name('a.b.c.d').split('.')), 2)
        self.assertEqual(len(
            clean_file_name('a=b=c=d.e').split('=')), 2)
        self.assertTrue(clear_file_name('a.b').startswith(
            GCODE_FOLDER_PREFIX))
        self.assertFalse(re.search(r'\w',
            clear_file_name('\ta\n b. \tc')))
        self.assertGreater(
            clear_file_name('a.b.c').count('-'), 4)


