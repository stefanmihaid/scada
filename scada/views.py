from django.shortcuts import render
from scada.models import Pole
from django.views import View
from django.http import HttpResponse
import ipdb


#user interaction class -- accepts get where all poles are presented to the user
#accepts post where the pole id is indicated and the rot speed

class UserInt(View):
    def get(self, request):
        a = Pole.objects.all()
        return HttpResponse(a.values())

    def post(self, request):
        #ipdb.set_trace()
        args = request.POST
        speed = args['speed']
        pole_id = args['pole_id']
        pole = Pole.objects.filter(id=pole_id).first()
        pole.rotationspeed = speed
        pole.save()
        return HttpResponse("New speed =%s"%speed, status=200)


#communicate with the CHIP board through REST API. The CHIP board will pull regurlarly the data for it's speed and send 
#information on the sensor values
class PoleInteract(View):
    #get the rotation speed. This must return a value of 1-3 based on the DB value for pole.speed
    def get(self, request):
        #take from the request the pole id
        pole_id = args['pole_id']
        #find the pole with id x
        pole = Pole.objects.filter(id=pole_id).first()
        #find rotation speed
        speed = pole.rotationspeed
        return HttpResponse(speed, status=200)

    def post(self, request):









