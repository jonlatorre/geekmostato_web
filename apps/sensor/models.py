from django.db import models

# Create your models here.

def read_temp():
    import serial
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.readline()
    ser.readline()
    ser.write('g')
    res = ser.readline()
    ser.close()
    return res

def set_temp(grado):
    import serial
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.readline()
    ser.readline()
    ser.write('s%s'%grado)
    res = ser.readline()
    ser.close()
    return res
