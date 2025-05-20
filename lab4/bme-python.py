import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
t = 1     # время в секундах
# или ser = serial.Serial(port, baudrate=baudrate)
ser.open()
x = []
start_time = time.monotonic()
end_time = start_time + 30

with open("HPTValues.txt", "w", encoding="utf-8") as file:
    while time.monotonic() < end_time:
        A = ser.read(56)
        print(A)
        file.write(str(A) + '\n')
        time.sleep(t)
        x.append(time.monotonic() - start_time)
    for i in range(len(x)):
        file.write(str(x[i]) + ' ')


