from django.shortcuts import render
from . import models

# Create your views here.
def index(req):
    if req.POST:
        plat = req.POST['name']
        wheel = req.POST['type']
        models.tugas.objects.create(name=plat, type=wheel)
        
    dataFetch = models.vehicle.objects.all()
    return render(req, 'index.html', {
		'list_vehicle' : dataFetch,
		})