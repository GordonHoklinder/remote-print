import unittest

from gcode_sender import GcodeSender

class GcodeSenderTests(unittest.TestCase):
    def setUp(self):
        self.gcode_sender = GcodeSender(None)

    def mock_send_gcode(self):
        self.gcode = ''
        self.result = 'ok'
        def mocker(gcode):
            self.gcode += gcode + '$'
            return self.result
        self.gcode_sender.send_gcode = mocker

    def test_start_file_printing(self):
        self.mock_send_gcode()
        self.assertEqual(self.gcode, '')
        self.gcode_sender.start_file_printing('file')
        self.assertEqual(self.gcode, r'M32 P !file$')

    def test_start_file_printing(self):
        self.mock_send_gcode()
        self.assertEqual(self.gcode, '')
        self.gcode_sender.send_file('G0\nG1 X\n', 'file')
        self.assertEqual(self.gcode, r'M28 file$G0$G1 X$M29 file$')

    def test_is_printing(self):
        self.mock_send_gcode()
        self.assertEqual(self.gcode, '')
        self.assertTrue(self.gcode_sender.is_printing())
        self.assertEqual(self.gcode, r'M27$')
        self.result = 'Not printing from file'
        self.assertFalse(self.gcode_sender.is_printing())



if __name__ == '__main__':
    unittest.main()
