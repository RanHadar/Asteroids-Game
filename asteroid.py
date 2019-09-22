#############################################################
# FILE : asteroid.py
# WRITERS :
# Amit Matityahu, amit2129, 209462969
# Ran Hadar, ranhadar, 305493389
# EXERCISE : intro2cs ex9 2016-2017
#############################################################

from screen import Screen
import copy
import math

INITIAL_SIZE = 3


SIZE_FACTOR = 20
NORMALIZING_FACTOR = -5
SECOND_POWER = 2


class Asteroid:
    def __init__(self, initial_pos, initial_speed, size):
        self.__pos = initial_pos
        self.__speed = initial_speed
        self.__size = size
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y

    def move(self):
        """
        This function adjusts
        the asteroids position

        returns None
        """

        delta_x = self.screen_max_x - self.screen_min_x
        delta_y = self.screen_max_y - self.screen_min_y

        self.__pos[0] = (self.__speed[0] + self.__pos[0] - self.screen_min_x) \
                        % delta_x + self.screen_min_x

        self.__pos[1] = (self.__speed[1] + self.__pos[1] - self.screen_min_y) \
                        % delta_y + self.screen_min_y

    def get_pos(self):
        """
        returns the pos

        returns list
        """
        return copy.deepcopy(self.__pos)

    def get_speed(self):
        """
        returns the speed

        returns list
        """
        return copy.deepcopy(self.__speed)

    def get_size(self):
        """
        returns the size

        returns int
        """
        return self.__size

    def get_radius(self):
        """
        returns the radius

        returns int
        """
        radius = self.__size * SIZE_FACTOR + NORMALIZING_FACTOR
        return radius

    def has_intersection(self, obj):
        """
        checking intersection with the received obj

        returns bool
        """
        obj_pos = obj.get_pos()
        asteroid_pos = self.get_pos()
        distance = math.sqrt((obj_pos[0] - asteroid_pos[0]) ** SECOND_POWER
                             + (obj_pos[1] - asteroid_pos[1]) ** SECOND_POWER)

        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False
