from django.db import models
import os
import serial

import logging
log = logging.getLogger("geekmostato")


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
    device = get_arduino_device()
    log.debug("vamos a leer la temp de %s"%device)
    ser = serial.Serial(device, serial_speed, timeout=1)
    ser.write('g')
    res = lectura()
    txt = ser.readline()
    log.debug("Hemos leido: %s"%txt)
    ser.close()
    try:
        lectura.temperatura, lectura.limite, lectura.encendida = txt.split(':')
    except:
        lectura.temperatura=0
        lectura.limite=0 
        lectura.encendida=0
    return res

def set_temp(grado):
    log.debug("vamos a mandar el limite: %s"%grado)
    ser = serial.Serial(get_arduino_device(), serial_speed, timeout=1)
    ser.readline()
    ser.readline()
    ser.write('s%s'%grado)
    res = ser.readline()
    log.debug("Hemos leido: %s"%res)
    ser.close()
    return res
