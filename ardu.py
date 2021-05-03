import serial
import time
import csv

ser = serial.Serial('/dev/ttyUSB0')
ser.flushInput()

for i in range(20):
    ser_bytes = ser.readline()
    decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    print(decoded_bytes)
