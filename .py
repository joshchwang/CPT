playerx = 20
playery = 299
vel = 20
playerw = 100
playerh = 100
isJump = False
jumpCounter = 10
Left = False
Right = False
timer = 500000
collisiony = 0

def setup():
    size(1200, 600)          
             
def draw():
    global playerx, playery, Right, Left, isJump, jumpCounter, mouseX, block1, collisiony
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
   
    if playerx >= 550 and playerx <= 750 and isJump == True:
        collisiony = 100
    elif playerx >= -10 and playerx <= 550:
        collisiony = 0
    elif playerx >=750 and playerx <= 1000000000:
        collisiony = 0
    rect(playerx-50, playery - collisiony, playerw, playerh)
    rect(-10, 400, 1500, 200) 
    

    
