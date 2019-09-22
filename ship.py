#############################################################
# FILE : ship.py
# WRITERS :
# Amit Matityahu, amit2129, 209462969
# Ran Hadar, ranhadar, 305493389
# EXERCISE : intro2cs ex9 2016-2017
#############################################################

from screen import Screen
import math
import copy

SHIP_RADIUS = 1
INITIAL_HEALTH = 3
INITIAL_HEADING = 0
PI_RADIANS_IN_DEGREES = 180
HEADING_CHANGE_RATE = 7
HEALTH_REDUCTION_RATE = 1


class Ship:
    def __init__(self, initial_pos, initial_speed):
        self.__pos = initial_pos
        self.__speed = initial_speed
        self.__heading = INITIAL_HEADING
        self.__radius = SHIP_RADIUS
        self.__health = INITIAL_HEALTH
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y

    def move(self):
        """
        This function adjusts
        the ships position

        returns None
        """

        self.get_speed()
        delta_x = self.screen_max_x - self.screen_min_x
        delta_y = self.screen_max_y - self.screen_min_y

        # calculating new coordinates
        self.__pos[0] = (self.__speed[0] + self.__pos[0] - self.screen_min_x) \
                        % delta_x + self.screen_min_x

        self.__pos[1] = (self.__speed[1] + self.__pos[1] - self.screen_min_y) \
                        % delta_y + self.screen_min_y

    def accelerate(self, up):
        """
        this function adjusts the ships
        speed if the user pressed up

        receives bool:
        returns None
        """
        if up:
            self.__speed[0] += math.cos((math.pi * self.__heading)
                                        / PI_RADIANS_IN_DEGREES)
            self.__speed[1] += math.sin((math.pi * self.__heading)
                                        / PI_RADIANS_IN_DEGREES)

    def set_heading_left(self, left):
        """
        this function adjusts the ships heading
        counterclockwise if user pressed left key

        receives bool:
        return None
        """

        if left:
            self.__heading += HEADING_CHANGE_RATE  # magic number

    def set_heading_right(self, right):
        """
        this function adjusts the ships heading
        clockwise if user pressed right key

        receives bool:
        return None
        """

        if right:
            self.__heading -= HEADING_CHANGE_RATE

    def shoot_torpedo(self, space):
        """
        gets the current ship pos, speed, heading to create a torpedo
        if user pressed the space key
        receives obj, bool
        returns (list, list, int)
        """

        if space:
            pos = self.get_pos()
            speed = self.get_speed()
            heading = self.get_heading()
            return pos, speed, heading

    def get_radius(self):
        """
        returns the radius

        returns int
        """
        return self.__radius

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
        return self.__speed

    def get_heading(self):
        """
        returns the heading

        returns int
        """
        return self.__heading

    def take_damage(self):
        """
        this function reduces ship health

        returns None
        """
        self.__health -= HEALTH_REDUCTION_RATE

    def get_health(self):
        """
        this function gets the ships health

        returns int
        """
        return self.__health


ship1 = Ship([0, 0], [0, 0])
