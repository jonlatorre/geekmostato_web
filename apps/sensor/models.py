from django.db import models
# Create your models here.

class lectura():
    temperatura = 0
    limite = 0
    encendida = False

def read_temp():
    import serial
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.readline()
    ser.readline()
    ser.write('g')
    res = lectura()
    txt = ser.readline()
    ser.close()
    lectura.temperatura, lectura.limite, lectura.encendida = txt.split(':')
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
