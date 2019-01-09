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

def setup():
    size(1200, 600)

def draw():
    global playerx, playery, Right, Left, isJump, jumpCounter, blockx, coinlistx, coinlisty, mouseX, deathcounter, death
    background(255)

    if not(mouseX + playerw / 2 > blockx and mouseX - playerw / 2 < blockx + 100 and
            playery >= 300 and playery < 300 + 50):
        blockx -= 1
        playerx = mouseX
        if mousePressed:
            isJump = True
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

    # if mouseX >  600:
    #     Right = True
    # if mouseX < 600:
    #     Left = True
    # if Left == True:
    #     playerx -= vel
    # if Right == True:
    #     playerx += vel

    # if playerx in coinlistx and marioy in coinlisty:
    #     print 'WORKING'

    rect(playerx - playerw / 2, playery, playerw, playerh)
    rect(-10, 400, 1500, 200)
    rect(blockx, 300, 100, 50)
    
    
    #Death Code

if death == True:
    time.freeze
    #ADD DEATH GIF U STUPID
    #FLOWER 
    #UPTOWN
    #CAT
    #KANGAROO
        
        
        
        
        
        
        
        
        
        
        
        
        
        
