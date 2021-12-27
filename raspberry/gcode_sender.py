from dataclasses import dataclass
import os


@dataclass
class GcodeSender:
    prusa: None

    def send_gcode(gcode: str) -> str:
        pass

    def send_file(gcodes: str, filename: str):
        # Start writing to a file.
        send_gcode(f'M28 {filename}')

        for gcode in gcodes.split('\n'):
            send_gcode(gcode)

        # Stop writing to a file.
        send_gcode(f'M29 {filename}')

    def start_file_printing(filename: str):
        send_gcode(f'M32 P !{filename}')

    def is_printing():
        return 'Not' not in send_gcode('M27')

    def print_file(gcodes: str, filename: str):
        send_file(gcodes, filename)
        start_file_printing(filename)

