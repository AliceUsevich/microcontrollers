import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
t = 1     # время в секундах
# или ser = serial.Serial(port, baudrate=baudrate)
ser.open()

while True:
    ser.write('Hello, world!'.encode('utf-8'))
    print(ser.read(13))
    time.sleep(t)