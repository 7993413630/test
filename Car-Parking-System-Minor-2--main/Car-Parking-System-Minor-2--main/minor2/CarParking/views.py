from django.shortcuts import render
from .models import CarParkingSpace

def home(request):
    return render(request, 'homepage.html')


def cps(request):
    if request.method == 'POST':
        req = request.POST['query'].upper().split()
        query = ''.join(i for i in req)
        flag = False
        data = {}
        if CarParkingSpace.objects.filter(area = query).exists():
            flag = True
            data = CarParkingSpace.objects.filter(area = query).values()
        return render(request, 'company.html', {'data' : data, 'flag' : flag})
    else:
        return render(request, 'company.html')
