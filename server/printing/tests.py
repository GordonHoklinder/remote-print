from django.test import TestCase

import re
import os

from .controllers import *

# Create your tests here.
class ControllerTest(TestCase):
    def setUp(self):
        GCODE_FOLDER_PREFIX = '/testing-files/'
        TSV_PATH = GCODE_FOLDER_PREFIX + 'in-queue.tsv'
        LOG_PATH = GCODE_FOLDER_PREFIX + 'runtime-log.txt'
        STATE_PATH = GCODE_FOLDER_PREFIX + 'state.txt'
        if os.path.exists(TSV_PATH):
            os.remove(TSV_PATH)
        if os.path.exists(LOG_PATH):
            os.remove(LOG_PATH)
        if os.path.exists(STATE_PATH):
            os.remove(STATE_PATH)

    def test_clear_file_name(self):
        clear_file_name('')
        self.assertEqual(len(
            clear_file_name('a.b.c.d').split('.')), 2)
        self.assertEqual(len(
            clear_file_name('a=b=c=d.e').split('=')), 2)
        self.assertTrue(clear_file_name('a.b').startswith(
            GCODE_FOLDER_PREFIX))
        self.assertFalse(re.search(r'\s',
            clear_file_name('\ta\n b. \tc')))
        self.assertGreater(
            clear_file_name('a.b.c').count('-'), 4)
        self.assertTrue('hell_o'  in clear_file_name('hell\t\n o.gcode'))

    def test_add_file_path(self):
        self.assertFalse(os.path.exists(TSV_PATH))
        add_file_path('path')
        self.assertTrue(os.path.exists(TSV_PATH))
        add_file_path('tests\nare\ngood')
        with open(TSV_PATH, 'r') as file:
            self.assertEqual(file.read(), 'path\ntests\nare\ngood\n')
        os.remove(TSV_PATH)

    def test_read_file(self):
        path = GCODE_FOLDER_PREFIX + 'test_file'
        self.assertIsNone(read_file(path))
        test_string = 'file content\nsecond\tline\n'
        with open(path, 'w') as file:
            file.write(test_string)
        self.assertEqual(read_file(path), test_string)
        os.remove(path)

    def test_get_printing_state(self):
        self.assertEqual(get_printing_state(), 'idle')
        test_string = 'printing'
        with open(STATE_PATH, 'w') as file:
            file.write(test_string)
        self.assertEqual(get_printing_state(), test_string)
        os.remove(STATE_PATH)



