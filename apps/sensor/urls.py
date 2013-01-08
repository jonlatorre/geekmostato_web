from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns("",
    url(r"^get/$", leer , name="sensor_get"),
    url(r"^set/(\d{1})/$", escribir , name="sensor_set"),
    url(r"^$", direct_to_template, {"template": "sensor/index.html"}, name="sensor_index"),
)
