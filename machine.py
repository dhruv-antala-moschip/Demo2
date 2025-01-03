import serial
import time

ser= serial.Serial(port="/dev/ttyACM0", baudrate=9600, dsrdtr=True, rtscts=True)
def read_serial_and_wait_for_data(ser, expected_str, timeout=30):
    start_time = time.time()
    found = False
    data = ""
    while time.time() < (start_time + timeout):
        data += ser.readline().decode('utf-8')

        if expected_str in data:
            # print(f"Deem: {eval(f'if {expected_str} in {data}')}")
            print(f"Expected string: {expected_str} found in serial output: {data}")
            # print(data)
            # print(f"Value Before: {found}")
            found = True
            # print(f"Value After: {found}")
            break
        if expected_str not in data:
            print(f"Expected string: {expected_str} not found in serial output: {data}")
            break


cmd = ['ping', 'arduino','hello']
read_serial_and_wait_for_data(ser, "Serial communication started")

ser.write(f"{cmd[1]}\r\n".encode('utf-8'))
read_serial_and_wait_for_data(ser, "rocks")

dict1={"ping":"pong","arduino":"rocks","hello":"world"}
for k,v in dict1.items():
    ser.write(f"{k}\r\n".encode('utf-8'))
    read_serial_and_wait_for_data(ser,v)
