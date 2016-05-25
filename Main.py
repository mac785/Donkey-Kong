import pygame, sys, traceback, JumpMan, PlatformFile, Constants, BarrelFile
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

    global jumpMan, leftKeyPressed, rightKeyPressed, upKeyPressed, downKeyPressed, ledgeTest, barrel
    global barrelList, platformList, ledgeList, barrelWait

    jumpMan = JumpMan.JumpMan()
    objectsOnScreen.append(jumpMan)
    barrelList = []

    leftKeyPressed = False
    rightKeyPressed = False
    upKeyPressed = False
    downKeyPressed = False
    ledgeTest = False

    pygame.time.set_timer(USEREVENT + 1, 5000)

    platformList = []
    platform1 = PlatformFile.Platform()
    objectsOnScreen.append(platform1)
    platformList.append(platform1)
    platform1.x = 200
    platform1.y = 390
    platform1.width = 400

    platform2 = PlatformFile.Platform()
    objectsOnScreen.append(platform2)
    platformList.append(platform2)
    platform2.x = 315
    platform2.y = 340

    platform3 = PlatformFile.Platform()
    objectsOnScreen.append(platform3)
    platformList.append(platform3)
    platform3.x = 245
    platform3.y = 336

    platform4 = PlatformFile.Platform()
    objectsOnScreen.append(platform4)
    platformList.append(platform4)
    platform4.x = 175
    platform4.y = 332

    platform5 = PlatformFile.Platform()
    objectsOnScreen.append(platform5)
    platformList.append(platform5)
    platform5.x = 105
    platform5.y = 328

    platform6 = PlatformFile.Platform()
    objectsOnScreen.append(platform6)
    platformList.append(platform6)
    platform6.x = 35
    platform6.y = 324

    platform7 = PlatformFile.Platform()
    objectsOnScreen.append(platform7)
    platformList.append(platform7)
    platform7.x = 85
    platform7.y = 269

    platform8 = PlatformFile.Platform()
    objectsOnScreen.append(platform8)
    platformList.append(platform8)
    platform8.x = 155
    platform8.y = 265

    platform9 = PlatformFile.Platform()
    objectsOnScreen.append(platform9)
    platformList.append(platform9)
    platform9.x = 225
    platform9.y = 261

    platform10 = PlatformFile.Platform()
    objectsOnScreen.append(platform10)
    platformList.append(platform10)
    platform10.x = 295
    platform10.y = 257

    platform11 = PlatformFile.Platform()
    objectsOnScreen.append(platform11)
    platformList.append(platform11)
    platform11.x = 365
    platform11.y = 253

    platform12 = PlatformFile.Platform()
    objectsOnScreen.append(platform12)
    platformList.append(platform12)
    platform12.x = 315
    platform12.y = 198

    platform13 = PlatformFile.Platform()
    objectsOnScreen.append(platform13)
    platformList.append(platform13)
    platform13.x = 245
    platform13.y = 194

    platform14 = PlatformFile.Platform()
    objectsOnScreen.append(platform14)
    platformList.append(platform14)
    platform14.x = 175
    platform14.y = 190

    platform15 = PlatformFile.Platform()
    objectsOnScreen.append(platform15)
    platformList.append(platform15)
    platform15.x = 105
    platform15.y = 186

    platform16 = PlatformFile.Platform()
    objectsOnScreen.append(platform16)
    platformList.append(platform16)
    platform16.x = 35
    platform16.y = 182

    platform17 = PlatformFile.Platform()
    objectsOnScreen.append(platform17)
    platformList.append(platform17)
    platform17.x = 85
    platform17.y = 127

    platform18 = PlatformFile.Platform()
    objectsOnScreen.append(platform18)
    platformList.append(platform18)
    platform18.x = 155
    platform18.y = 123

    platform19 = PlatformFile.Platform()
    objectsOnScreen.append(platform19)
    platformList.append(platform19)
    platform19.x = 225
    platform19.y = 119

    platform20 = PlatformFile.Platform()
    objectsOnScreen.append(platform20)
    platformList.append(platform20)
    platform20.x = 295
    platform20.y = 115

    platform21 = PlatformFile.Platform()
    objectsOnScreen.append(platform21)
    platformList.append(platform21)
    platform21.x = 365
    platform21.y = 111

    platform22 = PlatformFile.Platform()
    objectsOnScreen.append(platform22)
    platformList.append(platform22)
    platform22.width = 350
    platform22.x = 175
    platform22.y = 56


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
        pass
    if not leftKeyPressed and not rightKeyPressed:
        jumpMan.vx = 0
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
    checkBarrelPlatformCollisions()
    checkJumpManBarrelCollisions()
    checkBarrelDie()
    checkVictory()


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

def checkVictory():
    if jumpMan.x < 50 and jumpMan.y < 50:
        jumpMan.iAmAlive = False
        quit()

def checkBarrelDie():
    global barrelList
    for b in barrelList:
        if b.x >= 390 and b.y > 300:
            b.iAmAlive = False
            b.x = 1000
            b.y = 1000

def checkJumpManBarrelCollisions():
    global jumpMan, barrelList
    for b in barrelList:
        if jumpMan.x - jumpMan.width / 2 < b.x + b.rad and \
                                jumpMan.x + jumpMan.width / 2 > b.x - b.rad and \
                                jumpMan.y - jumpMan.height / 2 < b.y + b.rad and \
                                jumpMan.y + jumpMan.height / 2 > b.y - b.rad / 2:
            jumpMan.x = 30
            jumpMan.y = 360

def checkJumpManPlatformCollisions():
    global jumpMan
    for p in platformList:
        if abs(jumpMan.x - p.x) < jumpMan.width / 2 + p.width / 2:
            # hitting from below...
            if jumpMan.vy < 0:  # moving up?
                if abs(jumpMan.y - p.y) < jumpMan.height / 2 + p.height / 2:
                #if p.y - jumpMan.y < jumpMan.height / 2 + p.height / 2 and p.y < jumpMan.y:
                    print "Bottom Hit"
                    jumpMan.vy = 0
                    # jumpMan.vy = abs(jumpMan.vy)
            elif jumpMan.vy > 0:  # moving down?
                if p.y - jumpMan.y < jumpMan.height / 2 + p.height / 2 and p.y > jumpMan.y:
                    print "Top Hit"
                    jumpMan.land()
                    jumpMan.y = p.y - p.height / 2 - jumpMan.height / 2

        # Check whether we hit the right edge of the platform....
        # 1) are we Jumping?
        # 2) Jumping to the left?
        # 3) Overlapping right edge of platform in x?
        # 4) Within 10 pixels of right edge of platform in x?
        # 5) Overlapping with bottom edge of platform?
        # 6) Overlapping with top edge of platform?
        if jumpMan.vx < 0 and \
                                jumpMan.x - jumpMan.width / 2 < p.x + p.width / 2 and \
                                jumpMan.x + jumpMan.width / 2 > p.x - p.width / 2 and \
                                jumpMan.y - jumpMan.height / 2 < p.y + p.height / 2 and \
                                jumpMan.y + jumpMan.height / 2 > p.y - p.height / 2:
            if jumpMan.status == Constants.STATUS_JUMPING:
                jumpMan.x = (p.x + p.width / 2) + jumpMan.width / 2
                print "Left Hit"
            if jumpMan.status == Constants.STATUS_WALKING:
                jumpMan.y -= 4

        # Check whether we hit the left edge of the platform....
        # 1) are we Jumping?
        # 2) Jumping to the right?
        # 3) Overlapping left edge of platform in x?
        # 4) Within 10 pixels of left edge of platform in x?
        # 5) Overlapping with bottom edge of platform?
        # 6) Overlapping with top edge of platform?

        elif jumpMan.vx > 0 and \
                                jumpMan.x - jumpMan.width / 2 < p.x + p.width / 2 and \
                                jumpMan.x + jumpMan.width / 2 > p.x - p.width / 2 and \
                                jumpMan.y - jumpMan.height / 2 < p.y + p.height / 2 and \
                                jumpMan.y + jumpMan.height / 2 > p.y - p.height / 2:
            if jumpMan.status == Constants.STATUS_JUMPING:
                jumpMan.x = (p.x - p.width / 2) - jumpMan.width / 2
                print "Left Hit"
            if jumpMan.status == Constants.STATUS_WALKING:
                jumpMan.y -= 4



        elif jumpMan.status == Constants.STATUS_WALKING:
            # I think I'm walking... is there any ground under my feet?
            isTouching = False
            for p in platformList:
                if abs(jumpMan.x - p.x) < jumpMan.width / 2 + p.width / 2 and abs(jumpMan.y - p.y) < jumpMan.height / 2 + p.height / 2 + 1:
                    isTouching = True

            if not isTouching:
                jumpMan.status = Constants.STATUS_JUMPING



def checkBarrelPlatformCollisions():
    global barrelList
    for barrel in barrelList:
        for p in platformList:
            if abs(barrel.x - p.x) < barrel.rad + p.width / 2:
                # hitting from below...
                if barrel.vy < 0:  # moving up?
                    if abs(barrel.y - p.y) < barrel.rad + p.height / 2:
                    #if p.y - jumpMan.y < jumpMan.height / 2 + p.height / 2 and p.y < jumpMan.y:
                        print "Bottom Hit B"
                        barrel.vy = 0
                        # jumpMan.vy = abs(jumpMan.vy)
                elif barrel.vy > 0:  # moving down?
                    if p.y - barrel.y < barrel.rad + p.height / 2 and p.y > barrel.y:
                        print "Top Hit B"
                        barrel.land()
                        barrel.y = p.y - p.height / 2 - barrel.rad

            # Check whether we hit the right edge of the platform....
            # 1) are we Jumping?
            # 2) Jumping to the left?
            # 3) Overlapping right edge of platform in x?
            # 4) Within 10 pixels of right edge of platform in x?
            # 5) Overlapping with bottom edge of platform?
            # 6) Overlapping with top edge of platform?
            if barrel.vx < 0 and \
                                    barrel.x - barrel.rad < p.x + p.width / 2 and \
                                    barrel.x + barrel.rad > p.x - p.width / 2 and \
                                    barrel.y - barrel.rad < p.y + p.height / 2 and \
                                    barrel.y + barrel.rad > p.y - p.height / 2:
                if barrel.status == Constants.STATUS_JUMPING:
                    barrel.x = (p.x + p.width / 2) + barrel.rad
                    print "Left Hit B"
                if barrel.status == Constants.STATUS_WALKING:
                    barrel.y -= 4

            # Check whether we hit the left edge of the platform....
            # 1) are we Jumping?
            # 2) Jumping to the right?
            # 3) Overlapping left edge of platform in x?
            # 4) Within 10 pixels of left edge of platform in x?
            # 5) Overlapping with bottom edge of platform?
            # 6) Overlapping with top edge of platform?

            elif barrel.vx > 0 and \
                                    barrel.x - barrel.rad < p.x + p.width / 2 and \
                                    barrel.x + barrel.rad > p.x - p.width / 2 and \
                                    barrel.y - barrel.rad < p.y + p.height / 2 and \
                                    barrel.y + barrel.rad > p.y - p.height / 2:
                if barrel.status == Constants.STATUS_JUMPING:
                    barrel.x = (p.x - p.width / 2) - barrel.rad
                    print "Left Hit B"
                if barrel.status == Constants.STATUS_WALKING:
                    barrel.y -= 4



            elif barrel.status == Constants.STATUS_WALKING:
                # I think I'm walking... is there any ground under my feet?
                isTouching = False
                for p in platformList:
                    if abs(barrel.x - p.x) < barrel.rad + p.width / 2 and abs(barrel.y - p.y) < barrel.rad + p.height / 2 + 1:
                        isTouching = True

                if not isTouching:
                    barrel.status = Constants.STATUS_JUMPING


# =====================  readEvents()
def readEvents():
    """
    checks the list of events and determines whether to respond to one.
    """
    global leftKeyPressed, rightKeyPressed, upKeyPressed, downKeyPressed, barrelList
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
        if evt.type == USEREVENT + 1:
            tempBarrel = BarrelFile.Barrel()
            objectsOnScreen.append(tempBarrel)
            barrelList.append(tempBarrel)

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
