from django.shortcuts import render
from cars.models import Car,Driver
from colorama import Fore,init,Style
init()
# Create your views here.

def car_detail(reuest,pk):
    owner=Driver.objects.get(pk=pk)
    car_obj=Car.objects.filter(owner=owner.id)
    context={
        "vechile_info":car_obj,
        "owner_info":owner,
        'x':'something'
    }
    print(Fore.BLUE, context,'Debug')
    print(Style.RESET_ALL)
    return render(reuest,"car_detail.html",context)
