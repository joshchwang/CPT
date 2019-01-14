floory = 600
playerx = 200
playerw = 100
playerh = 100
playery = floory + playerh - 1
vel = 20
isJump = False
jumpCounter = 10
Left = False
Right = False
enemyx = 800
coinlistx = [1, 20, 30, 40, 500, 123, 3423, 11, 343]
coinlisty = [20, 30, 40, 50, 60, 70, 80, 90, 100]
deathcounter = 0
death = False
keys_pressed = [False for key_code in range(256)]
collisiony = 200
enemyy = 500
platx = 600
platy = 500


def setup():
    size(1360, 700)


def draw():
    global playerx, playerw, playery, Right, Left, isJump
    global jumpCounter, enemyx, coinlistx, coinlisty
    global deathcounter, death, collisiony, keys_pressed
    background(135, 206, 250)
    fill('#228B22')
    textSize(50)
    text("It's always so hard to do the right thing,", 200, 200)
    text("But so easy to do the wrong thing.", 275, 250)
    if not(playery - collisiony == enemyy-1 and
            playerx + playerw > enemyx and
            playerx - playerw < enemyx ):  # redo
        enemyx -= 1
        if keys_pressed[87]:  # w
            pass
        if keys_pressed[32]:  # space
            isJump = True
        if keys_pressed[65]:  # a
            playerx -= vel
        if keys_pressed[83]:  # s
            pass
        if keys_pressed[68]:  # d
            playerx += vel
    else:
        death = True
        deathcounter += 1
        print 'collided'

    if isJump and jumpCounter >= -10:
        neg = 1
        if jumpCounter < 0:
            neg = -1
        playery -= jumpCounter ** 2 * .5 * neg
        jumpCounter -= 1

    else:
        isJump = False
        jumpCounter = 10

    rect(-10, floory, 1500, 200)
    rect(enemyx, floory-100, 100, 50)
    rect(platx, platy, 100, 10)
    rect(platx + 300, platy  - 20, 100,10)
    # Checking if platform collision
    #platx = 600
    #platy = 500
    
    if (playerx >= platx-100 and playerx <= platx+100 and 
        playery - collisiony < platy-1 or 
        playerx >= platx-100 and playerx <= platx+100 
        and playery - collisiony < platy-100 and isJump
        ):
            collisiony = 300
    elif (playerx >= platx-100+300 and playerx <= platx+100+300 and 
        playery - collisiony < platy-1-20 or 
        playerx >= platx-100+300 and playerx <= platx+100+300 
        and playery - collisiony < platy-100-20 and isJump ):
        collisiony = 320
    else:
        collisiony = 200

    # Player
    rect(playerx, playery - collisiony, playerw, playerh)

    # Death Code

    if death:
        pass
        # play gif and restart
    print playerx, playery - collisiony, enemyy-1
    

def keyPressed():
    keys_pressed[keyCode] = True


def keyReleased():
    keys_pressed[keyCode] = False
