from nose.tools import assert_equal
from parameterized import parameterized
from numbers_tasks.src.cost_of_tile_to_cover_WH_Floor import *
import unittest


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        (100, 150, 0.5, 7500),
        (200, 50, 0.1, 1000),
        (100, 15, 5, 7500)
    ])
    def test_simple_solution(self, height, width, cost, result):
        calc_function = simple_calc_function()
        assert_equal(calc_function(height, width, cost), result)


    @parameterized.expand([
        ({'floor_height':10, 'floor_width':15, 'tile_height':100, 'tile_width':150, 'tile_cost':15555},)
    ])
    def test_calc_function_raise_validation_exception_when_tile_is_bigger_then_floor(self, kwargs):
        self.assertRaises(TileValidateException, lambda: calc_function(**kwargs))


    @parameterized.expand([
        ({'floor_height': 150, 'floor_width': 100, 'tile_height': 100, 'tile_width': 90, 'tile_cost': 15555},)
    ])
    def test_calc_function_raise_validation_exception_when_can_not_place_tile_on_floor(self, kwargs):
        self.assertRaises(TileValidateException, lambda: calc_function(**kwargs))


    @parameterized.expand([
        (2000,{'floor_height': 100, 'floor_width': 150, 'tile_height': 10, 'tile_width': 15, 'tile_cost': 20}),
        (100,{'floor_height': 200, 'floor_width': 150, 'tile_height': 100, 'tile_width': 150, 'tile_cost': 50}),
        (625,{'floor_height': 10, 'floor_width': 15, 'tile_height': 2, 'tile_width': 3, 'tile_cost': 25}),
    ])
    def test_calc_function(self, result, kwarg):
        print(calc_function(**kwarg))
        self.assertEquals(calc_function(**kwarg), result)
