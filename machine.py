import serial
import time
import pandas as pd

ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600, dsrdtr=True, rtscts=True)

file = open("ard.txt", "w")
file.write("sr no., testcase ID, Command, Result, Status\n")
file.close()
# sr_no = 1
def read_serial_and_wait_for_data(index_val, ser, key21, expected_str, timeout=300):
    start_time = time.time()
    found = False
    data = ""
    while time.time() < (start_time + timeout):
        with open("ard.txt", "a") as f:
            data += ser.readline().decode('utf-8')
            if expected_str in data:
                # print(f"Expected string: '{expected_str}' found in serial output: {data} for {key21}")
                f.write(f"{int(index_val)},TC-{int(index_val)},{key21},Expected string: '{expected_str}',True\n")
                found = True
                break
            if not found:
                # print(f"Expected string: {expected_str} not found in serial output: {data}")
                f.write(f"{int(index_val)},TC-{int(index_val)},{key21},Expected: '{expected_str}' => o/p: 'Unknown Command',False\n")
                break


dic = {'ping': 'pong',
       'arduino': 'rocks',
       'hello': 'world',
       'name' : 'dev',
       "Arduino": "Rocks",
       "\\r\\n": 'pong'
    }

counter = 1
read_serial_and_wait_for_data(0, ser, "9600", "Serial communication started")

for key, value in dic.items():
    ser.write(f"{key}\r\n".encode('utf-8'))
    read_serial_and_wait_for_data(counter, ser, key, value)
    counter += 1

df = pd.read_csv('ard.txt')
df.to_excel('data.xlsx', index=False)
