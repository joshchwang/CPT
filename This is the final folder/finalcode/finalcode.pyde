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
sidescrol = 5
textx = 275
platformlist = [(0, 0), (300, 20), (760, 0),
                (1160, 50), (1560, 100),
                (1960, 120), (3000, 20), (3800, 20),
                (3400, 20), (3600, 0),
                (4500, 0), (4800, 120), (5200, 240), (5400, 260),
                (5600, 240), (5800, 250), (6000, 300)]
enemylist = [0]
holex = 3500
introx = 2000
homex = 8000
counter = 0
enemycounter = 0


def setup():
    size(1360, 700)
    global deathlist, deathimage, house, backgroundimage, herolist
    global hero1, enemyimagelist
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
                 death18, death19, death20, death21,
                 death22, death23, death24, death25,
                 death26, death27, death28, death29, death30]
    house = loadImage('TheBestCaveBoy.gif')
    backgroundimage = loadImage('BackgroundBoys.jpg')
    deathimage = death2
    hero1 = loadImage("hero1.gif")
    hero2 = loadImage("hero2.gif")
    hero3 = loadImage("hero3.gif")
    hero4 = loadImage("hero4.gif")
    hero5 = loadImage("hero5.gif")
    hero6 = loadImage("hero6.gif")
    hero7 = loadImage("hero7.gif")
    hero8 = loadImage("hero8.gif")
    hero9 = loadImage("hero9.gif")
    hero10 = loadImage("hero10.gif")
    hero11 = loadImage("hero11.gif")
    hero12 = loadImage("hero12.gif")
    hero13 = loadImage("hero13.gif")
    hero14 = loadImage("hero14.gif")
    hero15 = loadImage("hero15.gif")
    hero16 = loadImage("hero16.gif")
    hero17 = loadImage("hero17.gif")
    hero18 = loadImage("hero18.gif")
    hero19 = loadImage("hero19.gif")
    hero20 = loadImage("hero20.gif")
    hero21 = loadImage("hero21.gif")
    hero22 = loadImage("hero22.gif")
    hero23 = loadImage("hero23.gif")
    hero24 = loadImage("hero24.gif")
    hero25 = loadImage("hero25.gif")
    hero26 = loadImage("hero26.gif")
    hero27 = loadImage("hero27.gif")
    hero28 = loadImage("hero28.gif")
    herolist = [hero1, hero2, hero3, hero4, hero5, hero6, hero7,
                hero8, hero9, hero10,
                hero11, hero12, hero13, hero14, hero15,
                hero16, hero17, hero18, hero19,
                hero20, hero21, hero22, hero23, hero24, hero25,
                hero26, hero27, hero28]
    heroimage = hero1
    enemy1 = loadImage("enemy1.gif")
    enemy2 = loadImage("enemy2.gif")
    enemy3 = loadImage("enemy3.gif")
    enemy4 = loadImage("enemy4.gif")
    enemy5 = loadImage("enemy5.gif")
    enemy6 = loadImage("enemy6.gif")
    enemy7 = loadImage("enemy7.gif")
    enemy8 = loadImage("enemy8.gif")
    enemyimagelist = [enemy1, enemy2, enemy3, enemy4, enemy5,
                      enemy6, enemy7, enemy8]
    enemyimage = enemy1


def draw():
    global playerx, playerw, playery, Right, Left, isJump, trianglex
    global jumpCounter, enemyx, coinlistx, coinlisty, deathlist
    global deathcounter, death, collisiony, keys_pressed, platx, vel
    global textx, sidescrol, enemyy, floory, platy, playerh, triangley
    global holex, deathimage, deathlist, homex, house, counter, enemycounter

    noStroke()
    background(40, 46, 60)
    fill(80, 92, 124)
    font = loadFont('BlackadderITC-Regular-48.vlw')
    textFont(font)
    textSize(70)
    text("W A S D to move,", textx - 75 + 600, 200)
    text("Space to Jump", textx + 600, 250)
    fill('#0A0908')
    image(enemyimagelist[int(enemycounter)], enemyx, floory - 100, 100, 100)
    fill(80, 92, 124)
    image(herolist[int(counter)], playerx, playery-collisiony, playerw,
          playerh)

    if not(playery - collisiony == enemyy-1 and
           playerx + playerw > enemyx and
           playerx - playerw < enemyx):
            enemyx -= sidescrol + 1
            textx -= sidescrol
            platx -= sidescrol
            trianglex -= sidescrol
            holex -= sidescrol
            homex -= sidescrol
            if keys_pressed[32] and not (death):
                isJump = True
            if keys_pressed[65] and not(death):
                playerx -= vel
            if keys_pressed[68] and not(death):
                playerx += vel
            enemycounter += .1
            if enemycounter >= 8:
                enemycounter = 1
            counter += .4
            if counter >= 28:
                counter = 1
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
    rect(platx + 300, platy - 20, 100, 10)

# platformlist = [(0, 0), (300, 20), (760, 0),
#                 (1160, 50), (1560, 100),
#                 (1960, 120), (3000, 20), (3800, 20),
#                 (3400, 20), (3600, 0),
#                 (4500, 0), (4700, 120), (5100, 240)]

    for x, y in platformlist:
        rect(platx + x, platy - y, 100, 10)

    if (playerx >= platx - 100 and
        playerx <= platx + 100 and playery - collisiony < platy -
        1 or playerx >= platx - 100 and playerx <= platx +
            100 and playery - collisiony < platy-100 and isJump or isJump):
                collisiony = 300

        # plat2
    elif (playerx >= platx - playerh + 300 and playerx <= platx + playerh +
          300 and playery - collisiony < platy - 1 - 20 or
          playerx >= platx - playerh + 300 and playerx <= platx + playerh +
          300 and playery - collisiony < platy - playerw - 20 and isJump or
          isJump):
                collisiony = 320

        # plat3
    elif (playerx >= platx - 100 + 760 and playerx <= platx + 100 + 760 and
          playery - collisiony < platy-1 or
          playerx >= platx - 100 and playerx <= platx + 100 +
          760 and playery - collisiony < platy - 100 and isJump or
          isJump):
                collisiony = 300

        # plat4
    elif (playerx >= platx - 100 + 1160 and playerx <= platx + 100 + 1160 and
          playery - collisiony < platy-1 or
          playerx >= platx - 100 + 1060 and playerx <= platx + 100 +
          1160 and playery - collisiony < platy - 100 - 50 and isJump or
          isJump):
                collisiony = 350

        # plat5
    elif (playerx >= platx-100+1560 and playerx <= platx+100+1560 and
          playery - collisiony < platy - 1 or
          playerx >= platx-100+1560 and playerx <= platx + 100 +
          1560 and playery - collisiony < platy-100-100 and isJump or
          isJump):
                collisiony = 400

        # plat6
    elif (playerx >= platx-100+1960 and playerx <= platx+100+1960 and
          playery - collisiony < platy-1 or
          playerx >= platx-100+1960 and playerx <= platx+100 +
          1960 and playery - collisiony < platy-100-120 and isJump or isJump):
                collisiony = 420

        # plat7
    elif (playerx >= platx - 100 + 3000 and playerx <= platx + 100 + 3000 and
          playery - collisiony < platy-1 or
          playerx >= platx-100 + 3000 and playerx <= platx + 100 +
          3000 and playery - collisiony < platy-100 and isJump or
          isJump):
                collisiony = 320

        # plat 8
    elif (playerx >= platx-100+3600 and playerx <= platx+100+3600 and
          playery - collisiony < platy-1 or
          playerx >= platx-100+3600 and playerx <= platx+100 +
          3600 and playery - collisiony < platy-100 and isJump or
          isJump):
            collisiony = 300

        # plat9
    elif (playerx >= platx-100+3800 and playerx <= platx+100+3800 and
          playery - collisiony < platy-1 or
          playerx >= platx-100+3800 and playerx <= platx+100 +
          3800 and playery - collisiony < platy-100 and isJump or
          isJump):
                collisiony = 320

        # Pretty sure this is the death platform but I need conformation
    elif (playerx >= platx-100+5600 and playerx <= platx+100+5600 and
          playery - collisiony < platy-1 or
          playerx >= platx-100+5600 and playerx <= platx+100 +
          5600 and playery - collisiony < platy-100 and isJump or
          isJump):
                collisiony = 320
                death = True

        # plat10
    elif (playerx >= platx-100+4500 and playerx <= platx+100+4500 and
          playery - collisiony < platy-1 or
          playerx >= platx-100+4500 and playerx <= platx+100 +
          4500 and playery - collisiony < platy-100 and isJump or
          isJump):
                collisiony = 300

        # plat11
    elif (playerx >= platx-100+4800 and playerx <= platx+100+4800 and
          playery - collisiony < platy-1 or
          playerx >= platx-100+4800 and playerx <= platx+100 +
          4800 and playery - collisiony < platy-100 and isJump or
          isJump):
                collisiony = 420

        # plat12
    elif (playerx >= platx-100+5100 and playerx <= platx+100+5100 and
          playery - collisiony < platy-1 or
          playerx >= platx-100+5100 and playerx <= platx+100 +
          5100 and playery - collisiony < platy-100 and isJump or
          isJump):
            collisiony = 540
    else:
        collisiony = 200
    image(house, homex, floory - 700)
    while playerx >= homex + 50:
        playerx -= 10

    noStroke()
    textSize(700)
    textFont(font)
    text("Thanks for playing!", homex + 1200, 200)
    text("Please don't fail us!", homex + 1200, 250)

    # Player
    if (playerx + 100 >= trianglex and playerx + 100 < trianglex +
            1400 and playery >= triangley - 50):
        death
    fill('#0A0908')

    # level design "death"
    for difference in range(0, 1400, 50):
        triangle(trianglex + difference, triangley, trianglex + 25 +
                 difference, triangley - 50, trianglex + 50 +
                 difference, triangley)
        triangle(trianglex + difference + 4000, triangley, trianglex + 25 +
                 difference + 4000, triangley - 50, trianglex +
                 50 + difference + 4000, triangley)
        triangle(trianglex + difference + 4000, triangley - 200, trianglex +
                 25 + difference + 4000, triangley - 50 - 200, trianglex +
                 50 + difference + 4000, triangley - 200)

    if(playerx <= trianglex - 1400 and playery - collisiony +
       playerh >= triangley - 50 or playerx >= trianglex and playery -
       collisiony + playerh <= triangley - 50):
            death = True

    print(trianglex, playerx, triangley + playerh - 1 - 50,
          playery - collisiony)
    fill(80, 92, 124)
    text("Don't think too hard about this", textx + 2700, 200)
    rect(platx + 5000, platy - 100, 1400, 10)

    # annoying pit of death
    fill('#0A0908')
    rect(holex, floory, 900, 100)
    if (playerx >= holex and playerx <= holex + 900 and playery <=
            floory and not(isJump)):
            collisiony = 600
            death = True
    # if (playerx >= platx-100+5100 and playerx <= platx+100+5100 and
    #     playery - collisiony < platy-1  or
    #     playerx >= platx-100+5100 and playerx <= platx+100+5100
    #     and playery - collisiony < platy-100 and isJump or isJump):

    # Death Code
    if death:
        deathcounter += .3
        sidescrol = 0
        isJump = False
        if deathcounter >= 28:
            deathcounter = 0
        for d in (deathlist):
            deathimage = deathlist[int(deathcounter)]
            image(deathimage, width/2-148, height/2-133)
            if deathcounter == 28:
                deathcounter = 0
    if (playerx >= platx - 100 and playerx <= platx + 100 and
            playery - collisiony < platy - 1 or
            playerx >= platx - 100 and playerx <= platx +
            100 and playery - collisiony < platy-100 and isJump or
            isJump):
                collisiony = 300
    rect(platx + 5000, platy - 100, 1400, 10)

    if playery - collisiony <= floory:
        death

    if(playerx >= platx + 5000 and playerx <= platx + playerw + 6400 and
        playery - collisiony < platy - 1 or
        playerx >= platx - playerw + 5000 and playerx <= platx + playerw +
            6400 and playery - collisiony < platy - playerh and isJump):
            death = True


def keyPressed():
    keys_pressed[keyCode] = True


def keyReleased():
    keys_pressed[keyCode] = False
