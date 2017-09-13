"""
Find Cost of Tile to Cover W x H Floor

Calculate the total cost of tile it would take to cover a floor plan of width and height,
using a cost entered by the user.

Strange task and strange solutions in the internet. Too simple
"""

# TODO: raise exception if tiles can not be suited

def simple_calc_function ():
    return lambda height, width, cost : height * width * cost

def calc_function (**parameters):
    floor_height, floor_width, tile_height, tile_width, tile_cost = \
        parameters['floor_height'], parameters['floor_width'], parameters['tile_height'],\
        parameters['tile_width'], parameters['tile_cost']
    valid_square = valid(floor_height, floor_width, tile_height, tile_width)
    if valid_square :
        amount_of_tiles = calculate_amount(floor_height, floor_width, tile_height, tile_width)
        return amount_of_tiles * tile_cost
    else :
        return None

def valid (*parameters):
    if (parameters[0] < parameters[2]) or (parameters[1] < parameters[3]):
        return False
    elif (parameters[0] % parameters[2] != 0) or (parameters[1] % parameters[3] != 0):
        return False
    else :
        return True

def calculate_amount(*parameters):
    return (parameters[0] / parameters[2]) * (parameters[1] / parameters[3])
