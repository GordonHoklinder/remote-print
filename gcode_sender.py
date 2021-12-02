from dataclasses import dataclass
import os


@dataclass
class GcodeSender:
    prusa: None

    def send_gcode(gcode: str):
        pass

    def send_file(filepath: str, filename: str):
        with open(os.path.join(filepath, filename), 'r') as f:
            file = f.readlines()

        # Start writing to a file.
        send_gcode(f"M28 {filename}")

        for gcode in file:
            send_gcode(gcode)

        # Stop writing to a file.
        send_gcode(f"M29 {filename}")

    def print_file(filename: str):
        send_gcode(f"M32 P !{filename}")

#    def start_print():
#        send_gcode("M24")

#    def pause_print():
#        send_gcode("M25")

    def print(filepath: str, filename: str):
        send_file(filepath, filename)
        print_file(filename)
#        start_print()

