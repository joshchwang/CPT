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
enemyx = 1000
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
sidescrol = 2
textx = 275
platformlist = [(0, 0), (300, 20), (760, 0),
                (1160, 50), (1560, 100),
                (1960, 120), (3000, 20), (3800, 20),
                (3400, 20), (3600, 0)]
enemylist = [0]
holex = 3500
introx = 2000


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
    deathlist = [death2, death3, death4, death5,
                 death6, death7, death8, death9,
                 death10, death11, death12, death13,
                 death14, death15, death16, death17,
                 death18,death19, death20, death21,
                 death22,death23, death24, death25,
                 death26, death27, death28, death29, death30]
    playerimage = death2

def draw():
    global playerx, playerw, playery, Right, Left, isJump, trianglex
    global jumpCounter, enemyx, coinlistx, coinlisty, deathlist
    global deathcounter, death, collisiony, keys_pressed, platx, vel
    global textx, sidescrol, enemyy, floory, platy, playerh, triangley, holex
    background(250,250,210)
    noStroke()
    fill('#228B22')
    font = loadFont('BlackadderITC-Regular-48.vlw')
    textFont(font)
    textSize(70)
    text("It's always so hard to do the right thing,", textx - 75 + 300, 200)
    text("But so easy to do the wrong thing.", textx + 300, 250)
    
    for enemy in enemylist:
        rect(enemyx+enemy, floory-100, 100, 50)
        
    if not(playery - collisiony == enemyy-1 and
        playerx + playerw > enemyx and
        playerx - playerw < enemyx  ):  # redo
        enemyx -= sidescrol + 1
        textx -=  sidescrol
        platx -= sidescrol
        trianglex -= sidescrol
        holex -= sidescrol
        if keys_pressed[32]:  # space
            isJump = True
        
        if keys_pressed[65]:  # a
            playerx -= vel
        
        if keys_pressed[68]:  # d
            playerx += vel
    else:
        death = True

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
    
    rect(platx, platy, 100, 10)
    rect(platx + 300, platy  - 20, 100,10)

# platformlist = [(0, 0), (300, 20), (760, 0),
#                 (1160, 50), (1560, 100),
#                 (1960, 120), (3000, 20), (3800, 20),
#                 (3400, 20), (3600, 0)]   

    for x, y in platformlist:
        rect(platx + x, platy - y, 100, 10)
        
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
        #plat7
        
    elif (playerx>= platx-100+3000 and playerx <= platx+100+3000 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+3000 and playerx <= platx+100+3000
        and playery - collisiony < platy-100 and isJump or isJump):
        collisiony = 320
        #plat9
        
    elif (playerx >= platx-100+3800 and playerx <= platx+100+3800 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+3800 and playerx <= platx+100+3800
        and playery - collisiony < platy-100 and isJump or isJump):
        collisiony = 320
        #plat 8
        
    elif (playerx >= platx-100+3600 and playerx <= platx+100+3600 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+3600 and playerx <= platx+100+3600
        and playery - collisiony < platy-100 and isJump or isJump):
        collisiony = 300
        
    elif (playerx >= platx-100+5600 and playerx <= platx+100+5600 and 
        playery - collisiony < platy-1  or 
        playerx >= platx-100+5600 and playerx <= platx+100+5600
        and playery - collisiony < platy-100 and isJump or isJump):
        collisiony = 320
        
    else:
        collisiony = 200 
    
    # Player
    rect(playerx, playery - collisiony, playerw, playerh)
    stroke(12)
    noFill()
    rect(trianglex ,triangley-50, 1400, 50)
    
    if playerx + 100 >= trianglex and playerx + 100 < trianglex + 1400 and playery  >= triangley - 50:
        death
    print playerx, playery, trianglex, triangley
    fill('#228B22')
    #level design "death"
    for difference in range(0, 1400, 50):
        triangle(trianglex + difference, triangley,trianglex + 25+ difference,triangley - 50,trianglex + 50+ difference, triangley)
        triangle(trianglex + difference + 4000, triangley, trianglex + 25 + difference + 4000, triangley - 50, trianglex + 50 + difference + 4000, triangley) 
        triangle(trianglex + difference + 4000, triangley - 200,trianglex + 25 + difference + 4000, triangley - 50 - 200, trianglex + 50 + difference + 4000, triangley - 200  ) 
    
    fill('#228B22')
    text("Don't think too hard about this", textx + 3000, 200)         
    rect(platx + 5000, platy - 100, 1400,10)
    #annoying pit of death
    
    fill(1)
    rect(holex, floory, 400, 100)
    rect(holex + 400, floory, 500, 100)

    if playerx >= holex and playerx <= holex + 400 and collisiony == 200 and isJump == False:
        collisiony = 700
        death 
    elif playerx >= holex + 400 and playerx <= holex + 900 and collisiony == 200 and isJump == False:
        collisiony = 700
        death 
    
    # add triangle death on the lower layer
    
    # Death Code
    if death == True:
        deathcounter += .3
        sidescrol = 0
        if deathcounter >= 28:
            deathcounter = 0        
        for d in (deathlist):
            playerimage = deathlist[int(deathcounter)]
            image(playerimage, width/2-148, height/2-133)
            if deathcounter == 28:
                deathcounter = 0
    rect(platx + 5000, platy - 100, 1400,10)

    if playery <= floory:
        death

def keyPressed():
    keys_pressed[keyCode] = True


def keyReleased():
    keys_pressed[keyCode] = False
