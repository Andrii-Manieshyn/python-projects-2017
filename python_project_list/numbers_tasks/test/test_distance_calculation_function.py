from nose.tools import assert_equal
from parameterized import parameterized
from numbers_tasks.src.distance_calculation_function import *
import unittest


class ChangeReturnTestCase(unittest.TestCase):

    @parameterized.expand([
       #(lon1      , lat1     , lon2      , lat2     , units                  , result)
        (LonLatGeo(-77.037852, 38.898556), LonLatGeo(-77.043934, 38.897147), EarthRadius.KILLOMETERS, 0.549),
        (LonLatGeo(-77.037852, 38.898556), LonLatGeo(-77.043934, 38.897147), EarthRadius.MILES, 0.341),
        (LonLatGeo(42.037852, 38.898556),  LonLatGeo(52.043934, 38.897147), EarthRadius.MILES, 538.092),
        (LonLatGeo(42.037852, 38.898556),  LonLatGeo(52.043934, 38.897147), EarthRadius.KILLOMETERS, 865.756),
    ])
    def test_distance_between_two_points(self, first_point, second_point, units, result):
        assert_equal(haversin_formula(first_point, second_point, units)[1], result)

    @parameterized.expand([
       #(lon1      , lat1     , lon2      , lat2     , units                  , result)
        ("McGill University", "Tian'anmen, Beijing" , EarthRadius.KILLOMETERS, 18890.065),
        ("McGill University", "Tian'anmen, Beijing", EarthRadius.MILES, 11740.71),
    ])
    def test_distance_between_two_cities(self, first_city, second_city, units, result):
        assert_equal(haversin_formula(get_latlongs(first_city), get_latlongs(second_city), units)[1], result)
