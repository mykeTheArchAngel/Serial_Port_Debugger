# Serial_Port_Debugger
A practical Serial Port Enumeration &amp; Connection Tool. This tool helps identify active serial ports and connects to them for debugging hardware devices (like routers, IoT devices, or embedded systems), which is essential for electrical/hardware security testing.

Use with Real Hardware<br>
  1. Connect USB-to-Serial adapter<br>
  2. Identify device port:<br>
``sudo ./serial_tool.py --list``
Example output:
`` /dev/ttyUSB0 - FT232R USB UART ``

Connect to device:
``sudo ./serial_tool.py --connect /dev/ttyUSB0 --baud 115200 ``
