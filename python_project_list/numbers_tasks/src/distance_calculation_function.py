"""
Distance Between Two Cities

Calculates the distance between two cities and allows the user to specify a unit of distance.
This program may require finding coordinates for the cities like latitude and longitude.
"""
from math import *
from enum import Enum
from pygeocoder import Geocoder

class EarthRadius (Enum):
    KILLOMETERS = ('kilometers', 6373) # Earth radius in kilometers
    MILES = ('miles', 3961) # Earth radius in miles

class LonLatGeo:
    def __init__(self, lon, lat):
        self.longitude = lon
        self.latitude = lat

def haversin_formula(first_point, second_point, units):
    dlon = radians(second_point.longitude - first_point.longitude)
    dlat = radians(second_point.latitude - first_point.latitude)
    a = (sin(dlat / 2)) ** 2 + cos(radians(first_point.latitude)) * cos(radians(second_point.latitude)) \
                               * (sin(dlon / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = units.value[1] * c
    return ("Distance in %s " %  units.value[0], float(format(d, ".3f")))

def get_latlongs(location):
    coordinates = Geocoder.geocode(location)[0].coordinates
    point = LonLatGeo(coordinates[0], coordinates[1])
    return point
