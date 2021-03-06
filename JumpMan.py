__author__ = 'Jimmyjamz'
import pygame
import random
import Constants


class JumpMan:  # fix this... and then delete this comment.

    def __init__(self):
        """
        This automatically gets called when you first create this object.
        """
        self.x = 30
        self.y = 380
        self.vx = 0
        self.vy = 0
        self.iAmAlive = True
        self.timeSinceLastJump = 100
        self.width = 20
        self.height = 20
        self.status = Constants.STATUS_JUMPING
        self.timeSinceDeath = 0.0

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
        if self.status == Constants.STATUS_JUMPING:
            if self.timeSinceLastJump > Constants.JUMP_DURATION:
                color = pygame.Color(255, 255, 0)
            else:
                color = pygame.Color(255, 255, 255)
            pygame.draw.rect(surface, color, (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))
        elif self.status == Constants.STATUS_DYING:
            pass
            #color = pygame.Color(255, 0, 0)
            #pygame.draw.rect(surface, color, (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height), 2)
        elif self.status == Constants.STATUS_WALKING:
            color = pygame.Color(255, 255, 255)
            pygame.draw.rect(surface, color, (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))

    def step(self, deltaT):
        """
        this is called by the main loop and tells us to advance
        this object by one animation step - perhaps to move this
        object or change its appearance.
        :param deltaT: how long it has been since the last step.
        """
        self.x += self.vx * deltaT
        self.y += self.vy * deltaT

        if self.status != Constants.STATUS_WALKING:
            self.vy += Constants.JUMPMAN_VERT_ACCELERATION * deltaT
            if self.vy > Constants.JUMPMAN_MAX_VERT_VEL:
                self.vy = Constants.JUMPMAN_MAX_VERT_VEL

        if self.x >= 400 - self.width / 2:
            self.x = 400 - self.width / 2
        if self.x <= 0 + self.width / 2:
            self.x = 0 + self.width / 2
        if self.y >= 400 - self.height / 2:
            self.y = 400 - self.height / 2
        if self.y <= 0 + self.height / 2:
            self.y = 0 + self.height / 2
            self.vy = 1

    def moveLeft(self):
        self.x -= Constants.MOVE_DISTANCE
        self.vx = -1

    def moveRight(self):
        self.x += Constants.MOVE_DISTANCE
        self.vx = 1

    def jump(self):
        if self.status == Constants.STATUS_WALKING:
            self.status = Constants.STATUS_JUMPING
            self.vy -= Constants.JUMPMAN_JUMP_BOOST

    def land(self):
        self.status = Constants.STATUS_WALKING
        self.vy = 0

    def die(self):
        """
        This is how another object (or the main game) can tell
        this one it is time to go away. (Often used after a
         collision.)
        :return:
        """
        self.iAmAlive = False
