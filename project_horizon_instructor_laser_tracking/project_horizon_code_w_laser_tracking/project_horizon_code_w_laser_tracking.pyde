add_library('minim')
def setup():
    size(1000, 1000)
    #background
    global img, group
    img = loadImage('stars_in_the_night_sky_by_demykins.jpg') 
    group = loadImage("group picture.jpg")
     #MUSIC
    global img
    img = loadImage('stars_in_the_night_sky_by_demykins.jpg') 
    #SOUND
    minim= Minim(this)
    global explosion
    explosion = minim.loadFile('atari_boom5.wav')
    global pew
    pew = minim.loadFile('laser.aiff')
    global back
    back = minim.loadFile('Grey Sector v0_86.mp3')
    global music
    if back :
        back.play(0)
    global Gn
    Gn = minim.loadFile('atari_boom.wav')
    ## SHIELDS ##
    
    #shield
    global shield4_x, shield4_y, shield4
    shield4_x = 0
    shield4_y = 0
    shield4 = True 
    
    #shield3
    global shield3_x, shield3_y, shield3
    shield3_x = 0
    shield3_x = 0
    shield3 = True 
    
    #shield2
    global shield2_x, shield2_y, shield2
    shield2_x = 0
    shield2_x = 0
    shield2 = True 
    
    #shield1
    global shield1_x, shield1_y, shield1
    shield1_x = 0
    shield1_x = 0
    shield1 = True 
    
    ## BALLS ##
    
    #RED BALL
    global ellipse1_x, ellipse1_y, speedY, ellipse1_s, ellipse1Negative
    ellipse1_x = 0
    ellipse1_y = -450
    ellipse1_s = 32
    speedY = .5
    ellipse1Negative = False
    
    #GREEN BALL
    global ellipse5_x, ellipse5_y, speed5Y, ellipse5_s, ellipseNegative 
    ellipse5_x = 0
    ellipse5_y = 450
    ellipse5_s = 32
    speed5Y = .5
    
    #BLUE BALL
    global ellipse3_x, ellipse3_y, speed3X, ellipse3_s, ellipseNagative 
    ellipse3_x = 450
    ellipse3_y = 0
    ellipse3_s = 32
    speed3X = .5 
    
    #YELLOW BALL 
    global ellipse7_x, ellipse7_y, speed7X, ellipse7_s, ellipseNagative 
    ellipse7_x = -450
    ellipse7_y = 0
    ellipse7_s = 32 
    speed7X = -.5 
    
    global redBall, blueBall, greenBall, yellowBall
    
    redBall = True
    blueBall = True
    greenBall = True
    yellowBall = True
    
    ## SPRITE STUFF ##
    global sShip
    global sX, sY
    global theta
    global img 
    
   
    sShip  = loadImage("sShip.png") # If pulled from github directly, the image file and where the image should be accessed should be correct. If not, go to the repository and directly save the image into the correct folder
    imageMode(CENTER)
    sX = 0
    sY = 0
    theta = 0.01
    
    ## LASERS ##
    
    global laserX, laserY, laserW, laserH
    
    laserX = 0
    laserY = -3
    laserW = 100000
    laserH = 5
    
    global speed
    speed = 100
    
    global shoot
    shoot = False
    
    global red, green, blue
    red = 255
    green = 0
    blue = 0
    
    
    ## SCREENS ##
    global startUp, theGame, loseScreen, winScreen, instructions
    
    startUp = True
    theGame = False
    loseScreen = False
    winScreen = False
    instructions = False
    
    frameRate(100)

def get_coords(x, y):
    return (x - 500, -1 * (y - 500))

#DRAW

def draw():
    frameRate(100)
    smooth()
    
    global startUp, theGame, loseScreen, winScreen, instructions, img, group
    
    if mousePressed:
        startUp = False
        instructions = True
        theGame = False
    
    if startUp:
        image(img, 500, 500, 1000, 1000)
        fill(255)
        noStroke()
        triangle(500, 700, 500, 800, 580, 750)
        #fill(255, 0, 0)
        textSize(200)
        # RGB: HORIZON
        #fill(255, 0, 0)
        #stroke(255, 255, 255)
        fill(255, 0, 0)
        text('R', 300, 500)
        fill(0, 255, 0)
        text('G', 420, 500)
        fill(0, 0, 255)
        text('B', 560, 500)
        fill(255, 255, 0)
        text(':', 670, 480)
        fill(255, 255, 0)
        textSize(90)
        text('HORIZON', 310, 600)
        
        #Names 
        textSize(20)
        fill(255)
        text('By:', 195, 640)
        fill(255, 0, 0)
        text('Msontai Brock,', 230, 640)
        fill(0, 255, 0)
        text('Nikara Taylor,', 380, 640)
        fill(0, 0, 255)
        text('Brynn Jones,', 520, 640)
        fill(255, 255, 0)
        text('Mobolaji Ogunlade', 650, 640)

        
    if instructions:
        image(img, 500, 500, 1000, 1000)
        fill(254)
        stroke(154, 31, 96)
        rect(345, 345, 350, 350, 7)
        textSize(100)
        fill(0, 255, 0)
        text('PRESS', 510, 490)
        fill(255, 0, 0)
        text('Enter', 510, 600)
        
        ## HEADER ##
        textSize(50)
        textAlign(CENTER)
        # text("INSTRUCTIONS")
             
    if keyPressed:
        if key == ENTER:
            instructions = False
            theGame = True
    
    if theGame:
        global sShip, img
        global sX, sY
        global theta
        global laser
        global speed   
        global laserX, laserY, laserW, laserH
        global shoot
        global ball
        global redBall, blueBall, greenBall, yellowBall
        global ellipse1_s, ellipse5_s, ellipse3_s, ellipse7_s
        global red, green, blue
        
        global ellipse1_x, ellipse1_y, speedY, ellipse1Negative # Red Ball Variables
        global ellipse5_x, ellipse5_y, speed5Y, ellipseNegative # Green Ball Variables
        global ellipse3_x, ellipse3_y, speed3X, ellipseNagative # Blue Ball Variables
        global ellipse7_x, ellipse7_y, speed7X, ellipseNagative # Yellow Ball Variables
        
        translate(500, 500)    
        image(img,0,0)
        
        #calling the shield from setup
        global shield4_x, shield4_y, shield4
        global shield3_x, shield3_y, shield3
        global shield2_x, shield2_y, shield2
        global shield1_x, shield1_y, shield1
        #sheilds functions 
        if shield4:
            fill(255,0,0, 125)
            noStroke()
            ellipse(0,0,800,800)
        if (((ellipse1_x)**2 + (ellipse1_y)**2  or ((ellipse3_x)**2 + (ellipse3_y)**2) or ((ellipse5_x)**2 + (ellipse5_y)**2) or ((ellipse7_x)**2 + (ellipse7_y)**2))) < 422**2 and shield4 and (redBall or greenBall or blueBall or yellowBall):
            speedY = -speedY
            speed5Y = -speed5Y
            speed3X = -speed3X
            speed7X = -speed7X
            shield4 = False
            if Gn:
                Gn.play(0)
        if shield3:
            fill(0, 255, 0, 125)
            noStroke()
            ellipse(0,0,600,600)
        if (((ellipse1_x)**2 + (ellipse1_y)**2) or ((ellipse3_x)**2 + (ellipse3_y)**2) or ((ellipse5_x)**2 + (ellipse5_y)**2) or ((ellipse7_x)**2 + (ellipse7_y)**2)) < 322**2 and shield3 and (redBall or greenBall or blueBall or yellowBall):
            speedY = -speedY
            speed5Y = -speed5Y
            speed3X = -speed3X
            speed7X = -speed7X
            shield3 = False
            if Gn:
                Gn.play(0)
        if shield2:
            fill(0, 0, 255, 125)
            noStroke()
            ellipse(0,0,400,400)
        if (((ellipse1_x)**2 + (ellipse1_y)**2) or ((ellipse3_x)**2 + (ellipse3_y)**2) or ((ellipse5_x)**2 + (ellipse5_y)**2) or ((ellipse7_x)**2 + (ellipse7_y)**2)) < 222**2 and shield2 and (redBall or greenBall or blueBall or yellowBall):
            speedY = -speedY
            speed5Y = -speed5Y
            speed3X = -speed3X
            speed7X = -speed7X
            shield2 = False
            if Gn:
                Gn.play(0)
        if shield1:
            fill(255, 255, 0, 180)
            noStroke()
            ellipse(0,0,200,200)
        if (((ellipse1_x)**2 + (ellipse1_y)**2) or ((ellipse3_x)**2 + (ellipse3_y)**2) or ((ellipse5_x)**2 + (ellipse5_y)**2) or ((ellipse7_x)**2 + (ellipse7_y)**2)) < 122**2 and shield1 and (redBall or greenBall or blueBall or yellowBall):
            speedY = -speedY
            speed5Y = -speed5Y
            speed3X = -speed3X
            speed7X = -speed7X
            shield1 = False
            if Gn:
                Gn.play(0)
        
        
        #RED BALL
        # if ball 1 hit the outter circle at 500 then  bounce back... then come back down
        ellipse1_y = ellipse1_y - speedY 
        
        if redBall:
            fill(255,0,0)
            noStroke()
            ellipse(ellipse1_x, ellipse1_y, 50, 50)
            
        if ellipse1_y < -475:
            ellipseNegative = False 
            speedY = -speedY 
                
        #GREEN BALL
        #if ball 5 hits shield 4 at 800 then bounce back...
        ellipse5_y = ellipse5_y + speed5Y
            
        if greenBall:
            fill(0,255,0)
            noStroke()
            ellipse(ellipse5_x, ellipse5_y, 50, 50)
            
        if ellipse5_y > 475:
            ellipseNegative = False 
            speed5Y = -speed5Y 
        
        #BLUE BALL
        ellipse3_x = ellipse3_x + speed3X
        
        if blueBall:
            fill(0,0,255)
            noStroke()
            ellipse(ellipse3_x, ellipse3_y, 50, 50)
            
        if ellipse3_x > 475:
            ellipseNegative = False  
            speed3X = -speed3X
        
        #YELLOW BALL
        ellipse7_x = ellipse7_x + speed7X
        
        if yellowBall:
            fill(247,215,9)
            noStroke()
            ellipse(ellipse7_x, ellipse7_y, 50, 50)
            
        if ellipse7_x < -475:
            ellipseNegative = False 
            speed7X = -speed7X 
        
        #translate(500, 500)
        rotate(theta)
        image(sShip, sX, sY, 100, 100)
        
        if shoot:
            fill(254)
            stroke(red, green, blue)
            rect(laserX, laserY, laserW, laserH)
            
    if not redBall and not greenBall and not blueBall and not yellowBall:
        theGame = False
        winScreen = True
        back.pause()
        
    if (ellipse1_y >= -50) or (ellipse5_y <= 50) or (ellipse3_x <= 50) or (ellipse7_x >= -50):
        theGame = False
        loseScreen = True
        back.pause()

            
    ### RESULTS ###
    
    if loseScreen:
        background(0)
        image(img, 500, 500, 1000, 1000)
        image(group, 500, 450, 450, 450)
        fill(random(255),random(0),random(0))
        textSize(220)
        text("G",110,170)
        text("A",110,430)
        text("M",110,690)
        text("E",110,940)
        text("O",280,940)
        text("V",465,940)
        text("E",635,940)
        text("R",815,940)
        explosion.pause()

        
    if winScreen:
        background(0)
        image(img, 500, 500, 1000, 1000)
        image(group, 500, 230, 400, 400)
        fill(0,0,255)
        textSize(200)
        text("W",100,700)
        fill(255,0,0)
        textSize(200)
        text("I",260,700)
        fill(255,255,0)
        textSize(200)
        text("N",360,700)
        fill(0,0,255)
        textSize(200)
        text("N",500,700)
        fill(0,255,0)
        textSize(200)
        text("E",630,700)
        fill(255,0,0)
        textSize(200)
        text("R",740,700)
        fill(0,0,255)
        textSize(300)
        text("!",860,700)
        fill(0,255,0)
        textSize(300)
        text("!",890,700)
        fill(255,0,0)
        textSize(300)
        text("!",910,700)

        
# The Goal: To rotate with A and D
def keyPressed():
    frameRate(100)
    smooth()
    
    global sShip
    global sX, sY
    global theta
    global laser
    global speed   
    global laserX, laserY, laserW, laserH
    global shoot
    global ball
    global redBall, blueBall, greenBall, yellowBall
    global red, green, blue
    global ellipse1_s, ellipse5_s, ellipse3_s, ellipse7_s
    global pew, explosion , Gn
    
    if key == "a" or key == "A":
        theta -= .05 # This is similar to saying theta = theta - 0.05
        theta = theta % TWO_PI
    if key == "d" or key == "D":
        theta += .05 
        theta = theta % TWO_PI
    if key == " ": #laser shooting using spacebar
        if pew :
            pew.play(0)
        shoot = True
        testx = 0
        facingLeft = theta >= PI/2 and theta <= 3*(PI/2)
        while testx <= 500:
            testy = tan(2 * PI - theta) * testx* -1 ### Testing for the Red Ball
            if ((testx - ellipse1_x)**2 + (testy - ellipse1_y)**2) < (ellipse1_s/2)**2 and not facingLeft and (red == 255 and green == 0 and blue == 0): #Tests if theta is positive
                redBall = False
                red = 0
                green = 255
                blue = 0
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break
            testy = tan(2 * PI - theta) * testx
            if ((-testx - ellipse1_x)**2 + (testy - ellipse1_y)**2) < (ellipse1_s/2)**2 and facingLeft and (red == 255 and green == 0 and blue == 0): #Tests if theta is negative
                redBall = False 
                red = 0
                green = 255
                blue = 0
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break 
            testy = tan(2 * PI - theta) * testx* -1 ### Testing for the Green Ball
            if ((testx - ellipse5_x)**2 + (testy - ellipse5_y)**2) < (ellipse5_s/2)**2 and not facingLeft and (red == 0 and green == 255 and blue == 0): #Tests if theta is positive
                greenBall = False
                red = 0
                green = 0
                blue = 255
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break
            testy = tan(2 * PI - theta) * testx
            if ((-testx - ellipse5_x)**2 + (testy - ellipse5_y)**2) < (ellipse5_s/2)**2 and facingLeft and (red == 0 and green == 255 and blue == 0): #Tests if theta is negative
                greenBall = False 
                red = 0
                green = 0
                blue = 255
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break 
            testy = tan(2 * PI - theta) * testx* -1 ### Testing for the Blue Ball
            if ((testx - ellipse3_x)**2 + (testy - ellipse3_y)**2) < (ellipse3_s/2)**2 and not facingLeft and (red == 0 and green == 0 and blue == 255): #Tests if theta is positive
                blueBall = False
                red = 255
                green = 255
                blue = 0
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break
            testy = tan(2 * PI - theta) * testx
            if ((-testx - ellipse3_x)**2 + (testy - ellipse3_y)**2) < (ellipse3_s/2)**2 and facingLeft and (red == 0 and green == 0 and blue == 255): #Tests if theta is negative
                blueBall = False 
                red = 255
                green = 255
                blue = 0
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break 
            testy = tan(2 * PI - theta) * testx* -1 ### Testing for the Yellow Ball
            if ((testx - ellipse7_x)**2 + (testy - ellipse7_y)**2) < (ellipse7_s/2)**2 and not facingLeft and (red == 255 and green == 255 and blue == 0): #Tests if theta is positive
                yellowBall = False
                red = 255
                green = 0
                blue = 0
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break
            testy = tan(2 * PI - theta) * testx
            if ((-testx - ellipse7_x)**2 + (testy - ellipse7_y)**2) < (ellipse7_s/2)**2 and facingLeft and (red == 255 and green == 255 and blue == 0): #Tests if theta is negative
                yellowBall = False 
                red = 255
                green = 0
                blue = 0
                stroke(red, green, blue)
                if explosion :
                    explosion.play(0)
                break 
            testx += 1               
        
        
def keyReleased():
    frameRate(100)
    smooth()
    
    global sShip
    global sX, sY
    global theta
    global laser
    global speed   
    global laserX, laserY, laserW, laserH
    global shoot
    
    if key == " ":
        shoot = False

 ## END OF THE SPRITE STUFF ##
