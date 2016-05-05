#Test
import pygame, sys, traceback, JumpMan, BarrelFile
from pygame.locals import *

#import your classFiles here.

__author__ = 'Jimmyjamz'  #put your name here!!!
# =====================  pre-setup()
def preSetup():
    """
    stuff that gets done at the start of the game, common to all pygame projects
    we'll be doing.
    You shouldn't change this method (much) - you can play with screensize & font.
    """
    global buffer, debugFont, objectsOnScreen
    buffer = pygame.display.set_mode((224,256),pygame.DOUBLEBUF) #window size
    debugFont = pygame.font.SysFont("Helvetica", 12) #this is the font for
                                                    #the bottom of the screen.
    buffer.fill((128,0,255))
    pygame.display.flip()
    objectsOnScreen = [] #this is a list of all things that
                        # should be drawn on screen. It starts
                        # off empty, but we can add stuff to it.

# =====================  setup()
def setup():
    """
    This happens once in the program, at the very beginning.
    Unlike the "preSetup()" method, you are welcome to change this!
    """

    global jumpMan, leftKeyPressed, rightKeyPressed
    global barrelList, platformList

    jumpMan = JumpMan.JumpMan()
    objectsOnScreen.append(jumpMan)

    leftKeyPressed = False
    rightKeyPressed = False

    barrelList = []
    for i in range(0, 4):
        nextBarrel = BarrelFile.Barrel()
        barrelList.append(nextBarrel)
        objectsOnScreen.append(nextBarrel)

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

    debugDisplay(buffer,deltaT) #this makes the text at the bottom of the
                                #screen. Feel free to comment this line out.
    pygame.display.flip() # updates the window to show the latest
                          # version of the buffer.

# =====================  drawBackground()
def drawBackground():
    buffer.fill([0,0,128]) #clear screen with background color.
                           # (feel free to pick a different color.)
                           # (red, green, blue) 0-255.

    #alternately, you might later decide to blit in a background graphic.
# =====================  animateObjects()
def animateObjects(deltaT):
    """
    tells each object to step
    """
    if leftKeyPressed and not rightKeyPressed:
        pass
        """PLEASE FIX THIS JAMIE YOU DOOF"""
    if rightKeyPressed and not leftKeyPressed:
        pass
        """PLEASE FIX THIS JAMIE YOU DOOF"""
    for object in objectsOnScreen:
        if object.isDead():
            continue # skip the dead ones....
        object.step(deltaT)
# =====================  checkForInteractions()
def checkForInteractions():
    """
    this is where we test whether objects are interacting with
    one another.
    """
    checkJumpManBarrelCollisions()
    checkJumpManLadderClimb()
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
    for v in barrelList:
        if v.isDead():
            barrelList.remove(v)


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
    buffer.blit(objectCountSurface,(3,surface_rect.h-15))

    fpsSurface = debugFont.render("{0:3.1f} FPS".format(1 / deltaT), True, (255, 255, 255))
    buffer.blit(fpsSurface, ((surface_rect.w-5) - debugFont.size("{0:3.1f} FPS".format(1 / deltaT))[0], (surface_rect.h-15)))

# =====================  readEvents()
def readEvents():
    """
    checks the list of events and determines whether to respond to one.
    """
    global leftKeyPressed, rightKeyPressed
    events = pygame.event.get() #get the list of all events since the last time
                                #note: this list might be empty.
    for evt in events:
        if evt.type == QUIT: #We got an event! Is it telling us to quit???
            pygame.quit()
            raise Exception("User quit the game") # this exception will kick
                                                  # us out of the main loop at
                                                  # the bottom of the program.
        if evt.type == KEYDOWN:
            if evt.key == K_LEFT:
                leftKeyPressed = True
            if evt.key == K_RIGHT:
                rightKeyPressed = True
            if evt.key == K_UP:
                theOstrich.flap()

        if evt.type == KEYUP:
            if evt.key == K_LEFT:
                leftKeyPressed = False
            if evt.key == K_RIGHT:
                rightKeyPressed = False

            # You may decide to check other events, like the mouse
            # or keyboard here.
#---------------------------------------------------------------------------
# MAIN LOOP   <=======
#program start with game loop - this is what makes the loop() actually loop.
#---------------------------------------------------------------------------
pygame.init() #start up the pygame library

try: # we're about to try some behavior that might cause the
     # program to crash. If so, it will now jump to "except," below.

    preSetup() #do this (mandatory) stuff at the start of the game
    setup() #do this stuff once at the start of the game. - this is "your" setup.

    fpsClock = pygame.time.Clock() # this will let us pass the deltaT to loop.

    while True: #keep looping forever (or at least until the program crashes)

        loop(fpsClock.tick(60)/1000.0) #pass the time (in seconds) since the
                                       # last loop; max speed is 60fps.

        readEvents() #pay attention to the mouse and keyboard.


except Exception as reason: # if something goes wrong that
                            # causes the program to stop, let
                            # us know what's going on.

    if reason.message == "User quit the game": #exit gracefully
                                    #if the user closed the window
        print "Game over. User quit the game."
    else:                           #otherwise, give the programmer
                                    #some idea what happened.
        print "Exited program.",reason.message
        traceback.print_exc() #print what line the program was on
                              #when it crashed.
