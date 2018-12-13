playerx = 20
playery = 299
vel = 20
playerw = 100
playerh = 100
isJump = False
jumpCount = 10

def setup():
    size(1200, 600)


def keyPressed():
    global playerx, playery, isJump, jumpCount
    if key == 'a' and playerx > vel:
        playerx -= vel
    if key == 'd' and playerx < 1200 - playerw - vel:
        playerx += vel
    if not(isJump):
        if key == 'w':
            pass
        if key == 's':
            pass
        if key == 'r':
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            playery -= jumpCount **2 * .5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    print key
            
        
    
def draw():
    background(255)
    rect(playerx, playery, playerw, playerh)
    rect(-10, 400, 1500, 200)
