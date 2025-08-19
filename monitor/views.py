from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EnergyReading
from .serializers import EnergyReadingSerializer

@api_view(['POST'])
def add_reading(request):
    serializer = EnergyReadingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Reading added successfully'})
    return Response(serializer.errors)

@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'monitor/home.html')

@login_required(login_url='/login/')
def dashboard_view(request):
    readings = EnergyReading.objects.all().order_by('-timestamp')[:20][::-1]
    timestamps = [r.timestamp.strftime("%H:%M:%S") for r in readings]
    power_data = [r.power for r in readings]

    return render(request, 'monitor/dashboard.html', {
        'readings': readings,
        'timestamps': timestamps,
        'power_data': power_data
    })
