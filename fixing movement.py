
import time
playery = 300
vel = 20
playerw = 100
playerh = 100
isJump = False
jumpCounter = 10
Left = False
Right = False
blockx = 800
coinlistx = [1, 20, 30, 40, 500, 123, 3423, 11, 343]
coinlisty = [20, 30, 40, 50, 60, 70, 80, 90, 100]
deathcounter = 0
death = False
keys_pressed = [False for key_code in range(256)]

def setup():
    size(1200, 600)

def draw():
    global playerx, playery, Right, Left, isJump, jumpCounter, blockx, coinlistx, coinlisty, mouseX, deathcounter, death, collisiony, keys_pressed
    background(255)

    if keys_pressed[87]:  # w
        pass
    if keys_pressed[32]:  # space
        isJump = True
    if keys_pressed[65]:#a
        text('a', 50, 50)
    if keys_pressed[83]:#s
        text('s', 100, 50)
    if keys_pressed[68]:#d
        text('d', 150, 50)

    if not(mouseX + playerw / 2 > blockx and mouseX - playerw / 2 < blockx + 100 and
            playery >= 300 and playery < 300 + 50):
        blockx -= 1
        playerx = mouseX
    else:
        mouseX = blockx
        death = True
        deathcounter += 1

    if isJump == True and jumpCounter >= -10:
        neg = 1
        if jumpCounter < 0:
            neg = -1
        playery -= jumpCounter ** 2 * .5 * neg
        jumpCounter -= 1
    else:
        isJump = False
        jumpCounter = 10
    if mouseX >  600:
        Right = True
    if mouseX < 600:
        Left = True
    if Left == True:
        playerx -= vel
    if Right == True:
        playerx += vel

    # if playerx in coinlistx and marioy in coinlisty:
    #     print 'WORKING'

    rect(-10, 400, 1500, 200)
    rect(blockx, 300, 100, 50)
    rect(600,300,100,10)
    
    if playerx >= 550 and playerx <= 750 and isJump == True:
        collisiony = 100
    elif playerx >= -10 and playerx <= 550:
        collisiony = 0
    elif playerx >=750 and playerx <= 1000000000:
        collisiony = 0
        
    rect(playerx - playerw / 2, playery - collisiony, playerw, playerh)
    
    #Death Code

    if death == True:
        time.freeze
    #ADD DEATH GIF U STUPID
    #FLOWER 
    #UPTOWN
    #CAT
    #KANGAROO
    
def keyPressed():
    print(keyCode)
    keys_pressed[keyCode] = True

def keyReleased():
    keys_pressed[keyCode] = False
