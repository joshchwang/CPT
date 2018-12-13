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
    
    if mousePressed:
        global isJump, jumpCounter
        if isJump == True and jumpCounter >= -10:
            neg = 1
            if jumpCounter < 0 :
                neg = -1
            playery -= jumpCounter **2 *.5 * neg
            jumpCounter-=1
        else:
            isJump = False
            jumpCounter = 10
            
        global playerx, playery, Right, Left
        if mouseX >  600:
            Right = True   
        if mouseX < 600:
            Left = True
        if Left == True:
            playerx -= vel
        if Right == True:
            playerx += vel
    print mouseX
    background(255)
    rect(mouseX, playery, playerw, playerh)
    rect(-10, 400, 1500, 200)
