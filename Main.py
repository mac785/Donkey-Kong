import pygame, sys, traceback, JumpMan, PlatformFile, Constants
from pygame.locals import *

__author__ = 'Jimmyjamz'  # put your name here!!!


# =====================  pre-setup()
def preSetup():
    """
    stuff that gets done at the start of the game, common to all pygame projects
    we'll be doing.
    You shouldn't change this method (much) - you can play with screensize & font.
    """
    global buffer, debugFont, objectsOnScreen
    buffer = pygame.display.set_mode((400, 400), pygame.DOUBLEBUF)  # window size
    debugFont = pygame.font.SysFont("Helvetica", 12)  # this is the font for
    # the bottom of the screen.
    buffer.fill((128, 0, 255))
    pygame.display.flip()
    objectsOnScreen = []  # this is a list of all things that
    # should be drawn on screen. It starts
    # off empty, but we can add stuff to it.


# =====================  setup()
def setup():
    """
    This happens once in the program, at the very beginning.
    Unlike the "preSetup()" method, you are welcome to change this!
    """

    global jumpMan, leftKeyPressed, rightKeyPressed, upKeyPressed, downKeyPressed, ledgeTest
    global barrelList, platformList, ledgeList

    jumpMan = JumpMan.JumpMan()
    objectsOnScreen.append(jumpMan)

    leftKeyPressed = False
    rightKeyPressed = False
    upKeyPressed = False
    downKeyPressed = False
    ledgeTest = False

    platformList = []
    """platform1 = PlatformFile.Platform()
    objectsOnScreen.append(platform1)
    platformList.append(platform1)
    platform1.x = 200
    platform1.y = 390
    platform1.width = 400"""

    platform2 = PlatformFile.Platform()
    objectsOnScreen.append(platform2)
    platformList.append(platform2)
    platform2.x = 320
    platform2.y = 340

    platform3 = PlatformFile.Platform()
    objectsOnScreen.append(platform3)
    platformList.append(platform3)
    platform3.x = 250
    platform3.y = 336

    platform4 = PlatformFile.Platform()
    objectsOnScreen.append(platform4)
    platformList.append(platform4)
    platform4.x = 180
    platform4.y = 332


# =====================  loop()
def loop(deltaT):
    """
     this is what determines what should happen over and over.
     deltaT is the time (in seconds) since the last loop() was called.
     You probably should not change this method, though you can change
     the methods it calls.
    """
    drawBackground()
    animateObjects(deltaT)
    checkForInteractions()
    clearDeadObjects()
    drawObjects()

    debugDisplay(buffer, deltaT)  # this makes the text at the bottom of the
    # screen. Feel free to comment this line out.
    pygame.display.flip()  # updates the window to show the latest
    # version of the buffer.


# =====================  drawBackground()
def drawBackground():
    buffer.fill([0, 0, 128])  # clear screen with background color.
    # (feel free to pick a different color.)
    # (red, green, blue) 0-255.

    # alternately, you might later decide to blit in a background graphic.


# =====================  animateObjects()
def animateObjects(deltaT):
    """
    tells each object to step
    """
    global upKeyPressed, downKeyPressed
    if leftKeyPressed and not rightKeyPressed:
        jumpMan.moveLeft()
    if rightKeyPressed and not leftKeyPressed:
        jumpMan.moveRight()
    if upKeyPressed:
        jumpMan.jump()
    if downKeyPressed:
        jumpMan.y += 2
    for object in objectsOnScreen:
        if object.isDead():
            continue  # skip the dead ones....
        object.step(deltaT)


# =====================  checkForInteractions()
def checkForInteractions():
    """
    this is where we test whether objects are interacting with
    one another.
    """
    checkJumpManPlatformCollisions()
    # checkJumpManBarrelCollisions()
    # checkJumpManLadderClimb()


# =====================  clearDeadObjects()
def clearDeadObjects():
    """
    removes all objects that are dead from the "objectsOnScreen" list
    Note: this algorithm is written to be easier to understand, not necessarily
    to be the fastest code....
    """
    global objectsOnScreen

    for object in objectsOnScreen[:]:
        if object.isDead():
            objectsOnScreen.remove(object)


# =====================  drawObjects()
def drawObjects():
    """
    Draws each object in the list of objects.
    """
    for object in objectsOnScreen:
        object.drawSelf(buffer)


# =====================  debugDisplay()
def debugDisplay(buffer, deltaT):
    """
    displays possibly helpful information at the corners of
    the screen. Probably not something you'd want in a finished
    product.
    :param buffer: what we are going to draw into.
    :param deltaT: how much time since last update.
    """
    surface_rect = buffer.get_rect()
    objectCountSurface = debugFont.render("Objects: {0}".format(len(objectsOnScreen)), True, (255, 255, 255))
    buffer.blit(objectCountSurface, (3, surface_rect.h - 15))

    fpsSurface = debugFont.render("{0:3.1f} FPS".format(1 / deltaT), True, (255, 255, 255))
    buffer.blit(fpsSurface, ((surface_rect.w - 5) - debugFont.size("{0:3.1f} FPS".format(1 / deltaT))[0], (surface_rect.h - 15)))


def checkJumpManPlatformCollisions():
    global jumpMan
    if jumpMan.status == Constants.STATUS_JUMPING:
        for p in platformList:
            # Check whether we hit the right edge of the platform....
            # 1) are we Jumping?
            # 2) Jumping to the left?
            # 3) Overlapping right edge of platform in x?
            # 4) Within 10 pixels of right edge of platform in x?
            # 5) Overlapping with bottom edge of platform?
            # 6) Overlapping with top edge of platform?
            print jumpMan.vx
            if jumpMan.status == Constants.STATUS_JUMPING and \
                            jumpMan.vx < 0 and \
                                    jumpMan.x - jumpMan.width / 2 < p.x + p.width / 2 and \
                                    jumpMan.x + jumpMan.width / 2 > p.x - p.width / 2 and \
                                    jumpMan.y - jumpMan.height / 2 < p.y + p.height / 2 and \
                                    jumpMan.y + jumpMan.height / 2 > p.y - p.height / 2:
                print "Hit edge"
                jumpMan.vx *= -1
                # find out how much jumpMan's left edge is past the platform's right edge
                overlap = (p.x + p.width / 2) - (jumpMan.x - jumpMan.width / 2)
                # "bounce" jumpMan away from the right edge, by that amount.
                jumpMan.x = (p.x + p.width / 2) + jumpMan.width / 2 + overlap


            # Check whether we hit the left edge of the platform....
            # 1) are we Jumping?
            # 2) Jumping to the right?
            # 3) Overlapping left edge of platform in x?
            # 4) Within 10 pixels of left edge of platform in x?
            # 5) Overlapping with bottom edge of platform?
            # 6) Overlapping with top edge of platform?

            elif jumpMan.status == Constants.STATUS_JUMPING and \
                            jumpMan.vx > 0 and \
                                    p.x - jumpMan.x < jumpMan.width / 2 + p.width / 2 and \
                                    jumpMan.x + jumpMan.width / 2 < p.x - p.width / 2 + 10 and \
                                    jumpMan.y - p.y < jumpMan.height / 2 + p.height / 2 and \
                                    p.y - jumpMan.y < jumpMan.height / 2 + p.height:

                jumpMan.vx *= -1
                # find out how much jumpMan left edge is past the platform's right edge
                overlap = (jumpMan.x + jumpMan.width / 2) - (p.x - p.width / 2)
                # "bounce" jumpMan away from the right edge, by that amount.
                jumpMan.x = (p.x - p.width / 2) - jumpMan.width / 2 - overlap

            elif abs(jumpMan.x - p.x) < jumpMan.width / 2 + p.width / 2:
                # hitting from below...
                if jumpMan.vy < 0:  # moving up?
                    if abs(jumpMan.y - p.y) < jumpMan.height / 2 + p.height / 2 + 1:
                        jumpMan.vy = 0
                        # jumpMan.vy = abs(jumpMan.vy)
                elif jumpMan.vy > 0:  # moving down?
                    if p.y - jumpMan.y < jumpMan.height / 2 + p.height / 2 and p.y > jumpMan.y:
                        jumpMan.land()
                        jumpMan.y = p.y - p.height / 2 - jumpMan.height / 2

    elif jumpMan.status == Constants.STATUS_WALKING:
        # I think I'm walking... is there any ground under my feet?
        isTouching = False
        for p in platformList:
            if abs(jumpMan.x - p.x) < jumpMan.width / 2 + p.width / 2 and abs(jumpMan.y - p.y) < jumpMan.height / 2 + p.height / 2 + 1:
                isTouching = True

        if not isTouching:
            jumpMan.status = Constants.STATUS_JUMPING


# =====================  readEvents()
def readEvents():
    """
    checks the list of events and determines whether to respond to one.
    """
    global leftKeyPressed, rightKeyPressed, upKeyPressed, downKeyPressed
    events = pygame.event.get()  # get the list of all events since the last time
    # note: this list might be empty.
    for evt in events:
        if evt.type == QUIT:  # We got an event! Is it telling us to quit???
            pygame.quit()
            raise Exception("User quit the game")  # this exception will kick
            # us out of the main loop at
            # the bottom of the program.
        if evt.type == KEYDOWN:
            if evt.key == K_LEFT:
                leftKeyPressed = True
            if evt.key == K_RIGHT:
                rightKeyPressed = True
            if evt.key == K_UP:
                upKeyPressed = True
            if evt.key == K_DOWN:
                pass

        if evt.type == KEYUP:
            if evt.key == K_LEFT:
                leftKeyPressed = False
            if evt.key == K_RIGHT:
                rightKeyPressed = False
            if evt.key == K_UP:
                upKeyPressed = False
            if evt.key == K_DOWN:
                pass

                # You may decide to check other events, like the mouse
                # or keyboard here.


# ---------------------------------------------------------------------------
# MAIN LOOP   <=======
# program start with game loop - this is what makes the loop() actually loop.
# ---------------------------------------------------------------------------
pygame.init()  # start up the pygame library

try:  # we're about to try some behavior that might cause the
    # program to crash. If so, it will now jump to "except," below.

    preSetup()  # do this (mandatory) stuff at the start of the game
    setup()  # do this stuff once at the start of the game. - this is "your" setup.

    fpsClock = pygame.time.Clock()  # this will let us pass the deltaT to loop.

    while True:  # keep looping forever (or at least until the program crashes)

        loop(fpsClock.tick(60) / 1000.0)  # pass the time (in seconds) since the
        # last loop; max speed is 60fps.

        readEvents()  # pay attention to the mouse and keyboard.


except Exception as reason:  # if something goes wrong that
    # causes the program to stop, let
    # us know what's going on.

    if reason.message == "User quit the game":  # exit gracefully
        # if the user closed the window
        print "Game over. User quit the game."
    else:  # otherwise, give the programmer
        # some idea what happened.
        print "Exited program.", reason.message
        traceback.print_exc()  # print what line the program was on
        # when it crashed.
