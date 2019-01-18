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
trianglex = 1600
triangley = 600
sidescrol = 5
textx = 275
platformlist = [(0,0), (300,20), (760,0), (1160,50), (1560,100), (1960,120),(3000, 20), (3800, 20), (3400, 20) ]
holex = 3500


def setup():
    size(1360, 700)
    global playerimage, deathlist
    death2 = loadImage("2.gif")
    death3 = loadImage("3.gif")
    death4 = loadImage("4.gif")
    death5 = loadImage("5.gif")
    death6 = loadImage("6.gif")
    death7 = loadImage("7.gif")
    death8 = loadImage("8.gif")
    death9 = loadImage("9.gif")
    death10 = loadImage("10.gif")
    death11 = loadImage("11.gif")
    death12 = loadImage("12.gif")
    death13 = loadImage("13.gif")
    death14 = loadImage("14.gif")
    death15 = loadImage("15.gif")
    death16 = loadImage("16.gif")
    death17 = loadImage("17.gif")
    death18 = loadImage("18.gif")
    death19 = loadImage("19.gif")
    death20 = loadImage("20.gif")
    death21 = loadImage("21.gif")
    death22 = loadImage("22.gif")
    death23 = loadImage("23.gif")
    death24 = loadImage("24.gif")
    death25 = loadImage("25.gif")
    death26 = loadImage("26.gif")
    death27 = loadImage("27.gif")
    death28 = loadImage("28.gif")      
    death29 = loadImage("29.gif")
    death30 = loadImage("30.gif")
    deathlist = [ death2, death3, death4, death5, death6, death7, death8, death9, death10,
                death11, death12, death13, death14, death15, death16, death17, death18, death19,
                death20, death21, death22, death23, death24, death25, death26, death27, death28,
                death29, death30 ]
    playerimage = death2

def draw():
    global playerx, playerw, playery, Right, Left, isJump, trianglex
    global jumpCounter, enemyx, coinlistx, coinlisty, deathlist
    global deathcounter, death, collisiony, keys_pressed, platx, vel
    global textx, sidescrol, enemyy, floory, platy, playerh, triangley, holex
    background(135, 206, 250)
    noStroke()
    fill('#228B22')
    textSize(50)
    text("It's always so hard to do the right thing,", textx - 75, 200)
    text("But so easy to do the wrong thing.", textx, 250)
    
    if not(playery - collisiony == enemyy-1 and
            playerx + playerw > enemyx and
            playerx - playerw < enemyx ):  # redo
        enemyx -= sidescrol + 1
        textx -=  sidescrol
        platx -= sidescrol
        trianglex -= sidescrol
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
       # if keys_pressed[82]:  # r
            
    else:
        death = True
        deathcounter += .3
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
    
#platformlist = [(0,0), (300,20), (760,0), (1160,50), (1560,100), (1960,120)]

    for x, y in platformlist:
        rect(platx + x, platy - y, 100, 10)
        # if (playerx >= platx - 100 + x and playerx <= platx + 100 + x and 
        #    playery - collisiony < platy - 1 - y  or 
        #    playerx >= platx - 100 + x and playerx <= platx + 100 + x
        #    and playery - collisiony < platy - 100 - y and isJump or isJump ):
        #       collisiony = 300 + y

    if (playerx >= platx-100 and playerx <= platx+100 and 
        playery - collisiony < platy-1 or 
        playerx >= platx-100 and playerx <= platx+100 
        and playery - collisiony < platy-100 and isJump or isJump):
            collisiony = 300
        #plat2
    elif (playerx >= platx - 100 + 300 and playerx <= platx+100+300 and 
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
        playerx >= platx-100+1960 and playerx <= platx+100+1960
        and playery - collisiony < platy-100-120 and isJump or isJump):
        collisiony = 420
    elif (playerx >= platx-100+3000 and playerx <= platx+100+3000 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+3000 and playerx <= platx+100+3000
        and playery - collisiony < platy-100 and isJump or isJump):
        collisiony = 320
    elif (playerx >= platx-100+3800 and playerx <= platx+100+3800 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+3800 and playerx <= platx+100+3800
        and playery - collisiony < platy-100 and isJump or isJump):
        collisiony = 320
    else:
        collisiony = 200 
    
    # Player
    rect(playerx, playery - collisiony, playerw, playerh)
    
    noFill()
    stroke(10)
    rect(trianglex ,triangley-50, 1400, 50)
    if playerx >= trianglex and playerx < trianglex + 1400 and playery - collisiony == triangley - 50:
        death
    fill('#228B22')
    #level design "death"
    for difference in range(0, 1360, 50):
        triangle(trianglex + difference, triangley,trianglex + 25+ difference,triangley - 50,trianglex + 50+ difference, triangley)  
    
    playerx != -20

    #annoying pit of death
    fill(1)
    rect(holex, floory,400, 100)
    rect( holex + 400, floory, 500, 100)
    holex -= sidescrol
    if playerx >= holex and playerx <= holex + 400 and collisiony == 200 and isJump == False:
        playery = 0
        death = True
    elif playerx >= holex + 400 and playerx <= holex + 900 and collisiony == 200 and isJump == False:
        playery = 0
        death = True
    # Death Code
    if death == True:
        if deathcounter >= 28:
            deathcounter = 0        
        #Put in picture as failsafe
        for d in (deathlist):
            playerimage = deathlist[int(deathcounter)]
            image(playerimage, width/2-148, height/2-133)
            if deathcounter == 28:
                deathcounter = 0
    print playerx, playery - collisiony, enemyy-1
    
def keyPressed():
    keys_pressed[keyCode] = True


def keyReleased():
    keys_pressed[keyCode] = False
