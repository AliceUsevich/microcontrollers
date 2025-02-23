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

with open("Values.txt", "w", encoding="utf-8") as file:
    while time.monotonic() < end_time:
        V = ser.read(10)
        print(V)
        file.write(str(V) + '\n')
        time.sleep(t)
        x.append(time.monotonic() - start_time)
    for i in range(len(x)):
        file.write(str(x[i]) + ' ')


# while 1:
#     a = input()
#     if a == 'a':
#         ser.write(b'a')
#         with open("Volues.txt", "w", encoding="utf-8") as file:
#             while time.monotonic() < end_time:
#                 V = ser.read(10)
#                 print(V)
#                 file.write(str(V) + '\n')
#                 time.sleep(t)
#                 x.append(time.monotonic() - start_time)
#             for i in range(len(x)):
#                 file.write(str(x[i]) + ' ')
