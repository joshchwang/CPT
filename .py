playerx = 20
playery = 299
vel = 20
playerw = 100
playerh = 100
isJump = False
jumpCounter = 10
Left = False
Right = False


def setup():
    size(1200, 600)          
             
def draw():
    global playerx, playery, Right, Left, isJump, jumpCounter, mouseX
    playerx = mouseX
    if mousePressed:
        isJump = True
    if isJump == True and jumpCounter >= -10:
        neg = 1
        if jumpCounter < 0 :
            neg = -1
        playery -= jumpCounter **2 *.5 * neg
        jumpCounter-=1
    else:
        isJump = False
        jumpCounter = 10
    print playerx
    background(255)
     #collision
    rect(600,300,100,100)
    if playerx >= 550 and playery >=299 : 
        playerx = 550
    elif playerx >= 700 and playery <= 200:
        playery = 299
        playerx = 800
    elif playerx >= 550 and playerx <=700 and playery <=299:
        playery = 200
    elif playery <= 200 and playerx >= 550 and playerx >= 700  :
        playery = 299
 
    rect(playerx-50, playery, playerw, playerh)
    rect(-10, 400, 1500, 200)
