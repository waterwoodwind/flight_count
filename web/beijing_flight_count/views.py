from django.shortcuts import render
from django.http import HttpResponse
from beijing_flight_count.models import BeijingFlights
from django.core import serializers

import json

# Create your views here.
def home(request):
    return HttpResponse("home")


def beijing_flights(request):
    query_data = BeijingFlights.objects.all()
    json_data = serializers.serialize("json", BeijingFlights.objects.all())
    list_data = json.loads(json_data)

    upload_data = []
    for item in list_data:
        upload_data.append(item['fields'])
    upload_data = json.dumps(upload_data)
    return render(request, 'beijing_flights.html', {'json_data': upload_data})