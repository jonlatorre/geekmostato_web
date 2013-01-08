from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns("",
    url(r"^leer/$", leer , name="leer"),
    url(r"^set/(\d{1})/$", escribir , name="escribir"),
    #url(r"^$", direct_to_template, {"template": "geekmostato/index.html"}, name="index"),
)
