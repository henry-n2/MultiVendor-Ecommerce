import math
import requests
from datetime import datetime
from django.shortcuts import render
from .forms import SolarForm

def get_location(place_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={place_name}&count=5&language=en&format=json"
    response = requests.get(url).json()
    if "results" not in response:
        return None
    location = response["results"][0]
    return location["name"], location["latitude"], location["longitude"], location["admin1"]

def calculate_solar_angles(day_of_year, local_time, latitude):
    declination_angle = 23.45 * math.sin(math.radians((360 / 365) * (day_of_year - 81)))
    hour_angle = (local_time - 12) * 15
    zenith_angle = math.degrees(math.acos(math.cos(math.radians(latitude)) * math.cos(math.radians(declination_angle)) * math.cos(math.radians(hour_angle)) + math.sin(math.radians(latitude)) * math.sin(math.radians(declination_angle))))
    altitude_angle = 90 - zenith_angle
    return declination_angle, hour_angle, zenith_angle, altitude_angle

def calculate_GHI(zenith_angle):
    return max(1000 * math.cos(math.radians(zenith_angle)), 0)

def calculate_irradiance(zenith_angle):
    GHI = calculate_GHI(zenith_angle)
    DNI = GHI / max(math.cos(math.radians(zenith_angle)), 0.1) if GHI > 0 else 0
    DHI = GHI - DNI
    return GHI, DNI, DHI

def calculate_bill_units(bill_amount):
    slabs = [(5.18, 25), (5.69, 35), (6.7, 40), (7.45, 50), (7.62, 50), (7.62, 100), (9.21, float('inf'))]
    units, remaining = 0, bill_amount
    for rate, limit in slabs:
        if remaining < rate * limit:
            return units + int(remaining / rate)
        units += limit
        remaining -= rate * limit
    return units

def recommend_system(dni, available_area):
    if dni > 800 and available_area > 300:
        best_panel = "Monocrystalline"
    elif dni > 600:
        best_panel = "Polycrystalline"
    else:
        best_panel = "Thin-Film"

    if available_area > 500:
        best_mount = "Tracking System"
    elif 200 <= available_area <= 500:
        best_mount = "Fixed Tilt"
    else:
        best_mount = "Roof-Mounted System"

    return best_panel, best_mount

def solar_view(request):
    result = None

    if request.method == 'POST':
        form = SolarForm(request.POST)
        if form.is_valid():
            place_name = form.cleaned_data['place_name']
            electricity_bill = form.cleaned_data['electricity_bill']
            available_area = form.cleaned_data['available_area']
            near_water = form.cleaned_data['near_water']

            location = get_location(place_name)
            if not location:
                result = "Location not found. Try again."
            else:
                city, latitude, longitude, state = location
                day_of_year = datetime.now().timetuple().tm_yday
                local_time = datetime.now().hour
                _, _, zenith_angle, _ = calculate_solar_angles(day_of_year, local_time, latitude)
                GHI, DNI, DHI = calculate_irradiance(zenith_angle)

                total_units = calculate_bill_units(electricity_bill)
                total_capacity_required = round(total_units / 30 / 5, 2)
                total_panels = round(total_capacity_required / 0.4)
                total_area_required_m2 = round(total_panels * 2.2, 2)
                subsidy = 0.3 * total_panels * 40000
                total_cost = total_panels * 40000 - subsidy
                payback_period = round(total_cost / (electricity_bill * 12), 1)

                best_panel, best_mount = recommend_system(DNI, available_area)

                result = {
                    'city': city,
                    'state': state,
                    'latitude': latitude,
                    'DNI': DNI,
                    'best_panel': best_panel,
                    'best_mount': best_mount,
                    'total_panels': total_panels,
                    'total_cost': total_cost,
                    'payback_period': payback_period,
                }
    else:
        form = SolarForm()
    
    return render(request, 'solar_form.html', {'form': form, 'result': result})






