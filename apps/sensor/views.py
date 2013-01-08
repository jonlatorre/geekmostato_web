from django.shortcuts import render_to_response
from models import read_temp, set_temp

def leer(request):
    lectura = read_temp()
    return render_to_response('sensor/lectura.html', {'lectura': lectura})

def escribir(request, grado):
    lectura = set_temp(grado)
    return render_to_response('sensor/escribir.html', {'grado':grado, 'lectura': lectura})
