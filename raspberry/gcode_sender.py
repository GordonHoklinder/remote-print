import os
import serial
import time
import re

USB_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200

class GcodeSender:
    def __init__(self):
        self.prusa = serial.Serial(USB_PORT, BAUD_RATE, timeout=300)
        self.printing = False

    def read_response(self):
        response = ''
        # Wait until the ok message.
        while len(response) < 3 or response[-3:] != 'ok\n':
            response += self.prusa.read().decode()
        print(response)
        return response

    def send_gcode(self, gcode: str) -> str:
        print(gcode)
        self.prusa.write((gcode + '\n').encode())
        return self.read_response()

    def send_file(self, gcodes: str, filename: str):
        # Start writing to a file.
        #self.send_gcode(f'M28 {filename}')

        for gcode in gcodes.split('\n'):
            if gcode and not gcode.startswith(';'):
                self.send_gcode(gcode)

        # Stop writing to a file.
        #self.send_gcode(f'M29 {filename}')

    def start_file_printing(self, filename: str):
        self.send_gcode(f'M32 P !{filename}')

    def is_printing(self):
        return self.printing
        #return 'Not' not in self.send_gcode('M27')

    def print_file(self, gcodes: str, filename: str):
        self.printing = True
        self.send_gcode('G28')
        self.send_file(gcodes, filename)
        #self.start_file_printing(filename)
        #for chunk in re.findall('.'*100, gcodes):
        #    self.send_gcode(chunk)
        self.printing = False
