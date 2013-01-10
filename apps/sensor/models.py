from django.db import models
import os

DEVICE_LIST = {'/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyACM0', '/dev/ttyACM1'}
serial_speed = 57600

def get_arduino_device():
    for device in DEVICE_LIST:
        if os.path.exists(device):
            return device


class lectura():
    temperatura = 0
    limite = 0
    encendida = False

def read_temp():
    import serial
    ser = serial.Serial(get_arduino_device(), serial_speed, timeout=1)
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
    ser = serial.Serial(get_arduino_device(), serial_speed, timeout=1)
    ser.readline()
    ser.readline()
    ser.write('s%s'%grado)
    res = ser.readline()
    ser.close()
    return res
