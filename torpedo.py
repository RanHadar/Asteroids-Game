#############################################################
# FILE : torpedo.py
# WRITERS :
# Amit Matityahu, amit2129, 209462969
# Ran Hadar, ranhadar, 305493389
# EXERCISE : intro2cs ex9 2016-2017
#############################################################

from screen import Screen
import math
import copy



TORPEDO_RADIUS = 4
ACCELERATION_FACTOR = 2
RADIAN_CONVERSION = math.pi / 180
AGE_RATE = 1


class Torpedo:

    def __init__(self, initial_pos, ship_speed, initial_heading):
        self.__pos = initial_pos
        self.__heading = initial_heading
        self.__radius = TORPEDO_RADIUS
        self.__ship_speed = ship_speed
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.__speed = [0, 0]
        self.__age = 0

    def get_speed(self):
        """
        This function adjusts
        the torpedos position

        returns list
        """
        self.__speed[0] = self.__ship_speed[0] +\
                          ACCELERATION_FACTOR * math.cos(self.__heading *
                                                         RADIAN_CONVERSION)

        self.__speed[1] = self.__ship_speed[1] + \
                          ACCELERATION_FACTOR * math.sin(self.__heading *

                                                         RADIAN_CONVERSION)
        return copy.deepcopy(self.__speed)

    def move(self):
        """
        This function adjusts
        the torpedos position

        returns list
        """

        # torpedo age increases each time it moves
        self.__age += AGE_RATE

        self.get_speed()
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

    def get_heading(self):
        """
        returns the heading

        returns int
        """
        return self.__heading

    def get_radius(self):
        """
        returns the radius

        returns int
        """
        return self.__radius

    def get_age(self):
        """
        returns the torpedos age

        returns int
        """
        return self.__age
