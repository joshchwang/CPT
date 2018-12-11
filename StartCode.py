def setup():
    size (1200,600)
x=0
def keyPressed():
    global x
    if key == 'a':
        x -= 4
    if key == 'w':
        pass #jump
    if key == 'd':
        x += 4 
def draw():
    background(255)
    rect(x,300,100,100)
    rect(-10,400,1500,200)
