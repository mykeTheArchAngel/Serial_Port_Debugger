# List available serial ports
sudo ./serial_tool.py --list

# Connect to Arduino at 9600 baud
sudo ./serial_tool.py --connect /dev/ttyACM0

# Connect to router console at 115200 baud
sudo ./serial_tool.py --connect /dev/ttyUSB0 --baud 115200