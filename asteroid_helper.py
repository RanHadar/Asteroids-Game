#############################################################
# FILE : asteroid_helper.py
# WRITERS :
# Amit Matityahu, amit2129, 209462969
# Ran Hadar, ranhadar, 305493389
# EXERCISE : intro2cs ex9 2016-2017
#############################################################

from asteroid import Asteroid
from random import Random
from screen import Screen
INITIAL_SIZE = 3
MAX_INITIAL_SPEED = 2
MIN_INITIAL_SPEED = 1


max_x = Screen.SCREEN_MAX_X
max_y = Screen.SCREEN_MAX_Y
min_x = Screen.SCREEN_MIN_X
min_y = Screen.SCREEN_MIN_Y



def get_random_ship_loc():
    """
    this function generates random
    initial coordinates for ship

    returns list
    """
    initial_ship_pos = [0, 0]
    initial_ship_pos[0] = Random().randrange(min_x, max_x)
    initial_ship_pos[1] = Random().randrange(min_y, max_y)
    return initial_ship_pos


def initialize_asteroid_list(number_of_asteroids, ship_pos):
    """
    this function creates a list of asteroids
    with random speed and position

    receives int, list
    returns list
    """

    asteroid_list = list()

    for i in range(number_of_asteroids):

        initial_x_pos = Random().randrange(min_x, max_x)
        initial_y_pos = Random().randrange(min_y, max_y)

        # rerunning if an asteroid intersects with initial shop pos
        while initial_x_pos == ship_pos[0] or initial_y_pos == ship_pos[1]:
            initial_x_pos = Random().randrange(min_x, max_x)
            initial_y_pos = Random().randrange(min_y, max_y)

        initial_speeds = (-MAX_INITIAL_SPEED, -MIN_INITIAL_SPEED) + \
                         (MIN_INITIAL_SPEED, MAX_INITIAL_SPEED)

        initial_x_speed = Random().choice(initial_speeds)
        initial_y_speed = Random().choice(initial_speeds)

        asteroid_pos = [initial_x_pos, initial_y_pos]
        asteroid_speed = [initial_x_speed, initial_y_speed]

        # creating asteroid object
        asteroid = Asteroid(asteroid_pos, asteroid_speed, INITIAL_SIZE)
        asteroid_list.append(asteroid)

    return asteroid_list

