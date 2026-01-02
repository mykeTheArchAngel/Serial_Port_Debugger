cat > serial_tool.py << 'EOF'
#!/usr/bin/env python3
import serial
import serial.tools.list_ports
import argparse
import sys
import select  # CRITICAL IMPORT ADDED

def list_serial_ports():
    """List all available serial ports"""
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No serial ports found!")
        return
    
    print("\nAvailable Serial Ports:")
    print("=======================")
    for i, port in enumerate(ports, 1):
        print(f"{i}. {port.device} - {port.description}")
    print()

def connect_to_port(port_name, baud_rate=9600):
    """Connect to a serial port and provide interactive terminal"""
    try:
        ser = serial.Serial(
            port=port_name,
            baudrate=baud_rate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        print(f"\nConnected to {port_name} at {baud_rate} baud")
        print("Press Ctrl+C to exit\n")
        
        while True:
            # Read from serial
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting).decode('utf-8', errors='replace')
                sys.stdout.write(data)
                sys.stdout.flush()
            
            # Read from stdin
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                line = sys.stdin.readline()
                ser.write(line.encode())
                
    except serial.SerialException as e:
        print(f"\nError: {e}")
    except KeyboardInterrupt:
        print("\nDisconnected")
    finally:
        if 'ser' in locals():
            ser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serial Port Toolkit")
    parser.add_argument("-l", "--list", action="store_true", help="List available serial ports")
    parser.add_argument("-c", "--connect", metavar="PORT", help="Connect to specified serial port")
    parser.add_argument("-b", "--baud", type=int, default=9600, help="Baud rate (default: 9600)")
    
    args = parser.parse_args()
    
    if args.list:
        list_serial_ports()
    elif args.connect:
        connect_to_port(args.connect, args.baud)
    else:
        parser.print_help()
EOF