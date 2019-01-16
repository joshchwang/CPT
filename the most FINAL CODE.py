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
trianglex = 1360
triangley = 600
sidescrol = 0.7
textxx = 200
textx = 275

def setup():
    size(1360, 700)


def draw():
    global playerx, playerw, playery, Right, Left, isJump
    global jumpCounter, enemyx, coinlistx, coinlisty, textxx, textx
    global deathcounter, death, collisiony, keys_pressed, platx, trianglex
    background(135, 206, 250)
    noStroke()
    fill('#228B22')
    textSize(50)
    text("It's always so hard to do the right thing,", textxx, 200)
    text("But so easy to do the wrong thing.", textx, 250)
    textx -= sidescrol
    textxx -= sidescrol
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
    #plat1
    if (playerx >= platx-100 and playerx <= platx+100 and 
        playery - collisiony < platy-1 or 
        playerx >= platx-100 and playerx <= platx+100 
        and playery - collisiony < platy-100 and isJump or isJump):
            collisiony = 300
        #plat2
    elif (playerx >= platx-100+300 and playerx <= platx+100+300 and 
        playery - collisiony < platy-1-20 or 
        playerx >= platx-100+300 and playerx <= platx+100+300 
        and playery - collisiony < platy-100-20 and isJump or isJump):
        collisiony = 320
        #plat3
    elif (playerx >= platx-100 + 760 and playerx <= platx+100 + 760 and 
        playery - collisiony < platy-1 or 
        playerx >= platx-100 and playerx <= platx+100 + 760 
        and playery - collisiony < platy-100 and isJump or isJump):
        collisiony = 300
        #plat4
    elif (playerx >= platx-100+1160 and playerx <= platx+100+1160 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+1060 and playerx <= platx+100+1160
        and playery - collisiony < platy-100-50 and isJump or isJump):
        collisiony = 350
        #plat5
    elif (playerx >= platx-100+1560 and playerx <= platx+100+1560 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+1560 and playerx <= platx+100+1560
        and playery - collisiony < platy-100-100 and isJump or isJump):
        collisiony = 400
        #plat6
    elif (playerx >= platx-100+1960 and playerx <= platx+100+1960 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+19d60 and playerx <= platx+100+1960
        and playery - collisiony < platy-100-120 and isJump or isJump):
        collisiony = 420
    else:
        collisiony = 200

    # Player
    rect(playerx, playery - collisiony, playerw, playerh)
    
    #level design "death"
    for difference in range(0, 1360, 50):
        triangle(trianglex + difference, triangley,trianglex + 25+ difference,triangley - 50,trianglex + 50+ difference, triangley)  
    rect(platx + 760, platy, 100, 10)
    rect(platx + 1160, platy - 50, 100, 10)
    rect(platx + 1560, platy - 100, 100, 10)
    rect(platx + 1960, platy - 120, 100, 10)
    trianglex -= sidescrol
    # Death Code
    if death:
        pass
        # play gif and restart
    print playerx, playery - collisiony, enemyy-1
    platx -= sidescrol

def keyPressed():
    keys_pressed[keyCode] = True


def keyReleased():
    keys_pressed[keyCode] = False
