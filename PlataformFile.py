__author__ = 'Jimmyjamz'  # Update this!!!
import pygame
import random
import Constants.py


class className:  # fix this... and then delete this comment.

    def __init__(self):
        """
        This automatically gets called when you first create this object.
        """
        self.x = 200
        self.y = 300
        self.vx = 0
        self.vy = 0
        self.iAmAlive = True
        self.width = 20
        self.height = Constants.PLATFORM_HEIGHT

    def isDead(self):
        """
        this is a method used by the main loop to determine whether it
        is time to remove this object from the screen and the list of
        objects.
        :return: whether this object is dead now.
        """
        if self.iAmAlive:
            return False
        else:
            return True
            # alternative (1-line) version of this function:
            #  "return not self.iAmAlive"

    def drawSelf(self, surface):
        """
        this is called by the main loop and tells us to draw
        whatever this shape looks like onto the given surface.
        :param surface: what to draw on.
        """
        color = pygame.Color(128, 64, 0)
        pygame.draw.rect(surface, color, (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))

    def step(self, deltaT):
        """
        this is called by the main loop and tells us to advance
        this object by one animation step - perhaps to move this
        object or change its appearance.
        :param deltaT: how long it has been since the last step.
        """
        pass

    def die(self):
        """
        This is how another object (or the main game) can tell
        this one it is time to go away. (Often used after a
         collision.)
        :return:
        """
        self.iAmAlive = False
