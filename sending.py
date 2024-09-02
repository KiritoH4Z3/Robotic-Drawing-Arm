import serial
import time

# Adjust these based on your system
serial_port = 'COM3'  # For Windows; use '/dev/ttyUSB0' or '/dev/ttyACM0' for Linux
baud_rate = 9600
serial_connection = serial.Serial(serial_port, baud_rate)

# Function to send a command to the Arduino
def send_command(command):
    serial_connection.write(f"{command}\n".encode())
    time.sleep(0.1)  # Small delay to ensure Arduino has time to process each command

# Load the drawing instructions from the file
with open('drawing_instructions.txt', 'r') as f:
    drawing_instructions = f.readlines()

# Move the pen up initially
send_command("P0")

# Send instructions to Arduino
for instruction in drawing_instructions:
    x, y = instruction.strip().split(',')
    send_command(f"M{x},{y}")
    time.sleep(0.1)  # Small delay between movements

# Example pen down/up commands for final positioning
send_command("P1")  # Pen down
time.sleep(0.1)
send_command("P0")  # Pen up
time.sleep(0.1)

serial_connection.close()
print("Instructions sent to Arduino.")
