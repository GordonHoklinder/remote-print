import unittest

from gcode_sender import GcodeSender

class MockedGcodeSender(GcodeSender):
    def __init__(self):
        self.printing = False
        self.prusa = None
        self.gcode = ''

    def send_gcode(self, gcode):
        self.gcode += gcode + '$'


class GcodeSenderTests(unittest.TestCase):
    def setUp(self):
        self.gcode_sender = MockedGcodeSender()

    def test_send_gcodes(self):
        self.assertEqual(self.gcode_sender.gcode, '')
        self.gcode_sender.send_gcodes(
            'valid line\n; comment\nline with a comment; comment\n')
        self.assertEqual(self.gcode_sender.gcode, r'valid line$line with a comment; comment$')

    def test_print_file(self):
        self.assertEqual(self.gcode_sender.gcode, '')
        self.gcode_sender.print_file('')
        self.assertEqual(self.gcode_sender.gcode, r'G28$')



if __name__ == '__main__':
    unittest.main()
