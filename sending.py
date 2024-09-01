import serial
import time

# Adjust these based on your system
serial_port = 'COM3'  # For Windows; use '/dev/ttyUSB0' or '/dev/ttyACM0' for Linux
baud_rate = 9600
serial_connection = serial.Serial(serial_port, baud_rate)

# Load the drawing instructions from the file
with open('drawing_instructions.txt', 'r') as f:
    drawing_instructions = f.readlines()

# Send instructions to Arduino
for instruction in drawing_instructions:
    x, y = instruction.strip().split(',')
    serial_connection.write(f"M{x},{y}\n".encode())
    time.sleep(0.1)  # Small delay to ensure Arduino has time to process each command

# Example pen down/up commands
serial_connection.write("P1\n".encode())  # Pen down
time.sleep(0.1)
serial_connection.write("P0\n".encode())  # Pen up
time.sleep(0.1)

serial_connection.close()
print("Instructions sent to Arduino.")
