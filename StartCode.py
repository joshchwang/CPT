def setup():
    size (1200,600)
playerx = 20
playery = 300
vel = 20
playerw = 100
playerh = 100

def keyPressed():
    global playerx, playery
    if key == 'a' and playerx > vel:
        playerx -= vel
    if key == 'w':
        pass
    if key == 'd' and playerx < 1200 - playerw - vel:
        playerx += vel 

def draw():
    background(255)
    rect(playerx, playery, playerw,playerh)
    rect(-10,400,1500,200)
