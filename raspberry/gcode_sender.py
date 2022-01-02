from dataclasses import dataclass
import os


@dataclass
class GcodeSender:
    prusa: None

    def send_gcode(self, gcode: str) -> str:
        # Testing
        print(gcode)
        return 'ok'

    def send_file(self, gcodes: str, filename: str):
        # Start writing to a file.
        self.send_gcode(f'M28 {filename}')

        for gcode in gcodes.split('\n'):
            if gcode:
                self.send_gcode(gcode)

        # Stop writing to a file.
        self.send_gcode(f'M29 {filename}')

    def start_file_printing(self, filename: str):
        self.send_gcode(f'M32 P !{filename}')

    def is_printing(self):
        return 'Not' not in self.send_gcode('M27')

    def print_file(self, gcodes: str, filename: str):
        self.send_file(gcodes, filename)
        self.start_file_printing(filename)

