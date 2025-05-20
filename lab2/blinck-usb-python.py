import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
t = 1     # время в секундах
# или ser = serial.Serial(port, baudrate=baudrate)
ser.open()
ser.write(b'e')

while 1:
    ser.write(b'e')
    time.sleep(t)
    ser.write(b'd')
    time.sleep(t)




###
# ser.close()
# print(ser.is_open)

###
# port = "COM3"  # Replace with the appropriate COM port name
# baudrate = 9600  # Replace with the desired baud rate
# ser = serial.Serial(port, baudrate=baudrate)
# # Perform operations on the COM port
#
# ser.close()  # Remember to close the connection when done
#
# # Reading data
# data = ser.read(10)  # Read 10 bytes from the COM port
# print(data)
#
# # Writing data
# message = b"Hello, world!"  # Data to be sent, should be in bytes
# ser.write(message)