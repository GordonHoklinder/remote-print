import os
import serial
import time
import re

USB_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200

class GcodeSender:
    def __init__(self):
        self.prusa = serial.Serial(USB_PORT, BAUD_RATE, timeout=300)

    def read_response(self):
        response = ''
        # Wait until the ok message.
        while len(response) < 3 or response[-3:] != 'ok\n':
            response += self.prusa.read().decode()
        print(response)
        return response

    def send_gcode(self, gcode: str):
        print(gcode)
        self.prusa.write((gcode + '\n').encode())
        self.read_response()

    def send_gcodes(self, gcodes: str):
        for gcode in gcodes.split('\n'):
            # Skip comments and empty lines.
            if gcode and not gcode.startswith(';'):
                self.send_gcode(gcode)

    def print_file(self, gcodes: str):
        # Initialize head position
        self.send_gcode('G28')
        self.send_gcodes(gcodes)
