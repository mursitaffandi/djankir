from django.shortcuts import render
from . import models
from django.http import JsonResponse

# Create your views here.
def index(req):    
    dataFetch = models.vehicle.objects.all()
    return render(req, 'index.html', {
		'list_vehicle' : dataFetch,
		})

def exit(req):
    if 'outId' in req.POST:
        id = req.POST['outId']
        models.vehicle.objects.filter(pk=id).delete()

    dataFetch = models.vehicle.objects.all()
    return JsonResponse({'status': 200, 'message' : 'success', 'data' : dataFetch})

def enter(req):
    if 'plat' in req.POST and 'type' in req.POST:
        plat = req.POST['plat']
        wheel = req.POST['type']
        models.vehicle.objects.create(vehicle_name = plat, vehicle_wheels = wheel)
    
    dataFetch = models.vehicle.objects.all()
    return JsonResponse({'status': 200, 'message' : 'success', 'data' : dataFetch})