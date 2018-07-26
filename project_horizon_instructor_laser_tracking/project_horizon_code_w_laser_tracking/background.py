

def setup():
    size(1000, 1000)
    #background
    
    
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
    
    global startUp, theGame
    
    startUp = True
    theGame = False
    
    frameRate(100)

def get_coords(x, y):
    return (x - 500, -1 * (y - 500))

#DRAW

def draw():
    frameRate(100)
    smooth()
    global back
    
    global startUp, theGame
    
    if mousePressed:
        startUp = False
        theGame = True
    
    if startUp:
        background(0)
        fill(255)
        noStroke()
        rect(500, 500, 50, 50)
            
=======
# def setup():
#     size(1000, 1000)
#     global img 
#     img = loadImage('stars_in_the_night_sky_by_demykins.jpg')
#     background(255)
#     # global colors
#     # colors = [color(247,215,9, 190), color (0, 255, 0, 190), color(255, 0, 0, 190), color(0, 0, 255, 190)]
#     #ball 1
#     global ellipse1_x, ellipse1_y, speedY, ellipse1Negative
#     ellipse1_x = 500
#     ellipse1_y = 50
#     speedY = .5
#     ellipse1Negative = False
#     #ball 5
#     global ellipse5_x, ellipse5_y, speed5Y, ellipseNegative 
#     ellipse5_x = 500
#     ellipse5_y = 950
#     speed5Y = -.5
#     #ball 3
#     global ellipse3_x, ellipse3_y, speed3X, ellipseNagative 
#     ellipse3_x = 950
#     ellipse3_y = 500
#     speed3X = -.5 
#     #ball 7 
#     global ellipse7_x, ellipse7_y, speed7X, ellipseNagative 
#     ellipse7_x = 50
#     ellipse7_y = 500
#     speed7X = .5 
#     #shields 
#     #shield4
#     global shield4_x, shield4_y, shield4
#     shield4_x = 500
#     shield4_y = 500
#     shield4 = True 
#     #shield3
#     global shield3_x, shield3_y, shield3
#     shield3_x = 500
#     shield3_x = 500
#     shield3 = True 
#     #shield2
#     global shield2_x, shield2_y, shield2
#     shield2_x = 500
#     shield2_x = 500
#     shield2 = True 
#     #shield1
#     global shield1_x, shield1_y, shield1
#     shield1_x = 500
#     shield1_x = 500
#     shield1 = True 
#     #sprite 
    
# def draw():
#     background(255)
#     image(img,0,0)
#     fill(255)
#     ellipse(500, 500,25,25) 
#     #shields 
#     global shield4_x, shield4_y, shield4
#     global shield3_x, shield3_y, shield3
#     global shield2_x, shield2_y, shield2
#     global shield1_x, shield1_y, shield1
    
#     # # if ball 1, 3, 5, 7 hit shiled 4 shield 4 = False and breaks...
    
#     #sheilds functions 
#     if shield4:
#         fill(247,215,9, 190)
#         ellipse(500,500,800,800)
#     if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 412**2 and shield4:
#         print "Switch"
#         speedY = -speedY
#         speed5Y = -speed5Y
#         speed3X = -speed3X
#         speed7X = -speed7X
#         shield4 = False
#     if shield3:
#         fill(0, 255, 0, 180)
#         ellipse(500,500,600,600)
#     if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 312**2 and shield3:
#         print "Switch"
#         speedY = -speedY
#         speed5Y = -speed5Y
#         speed3X = -speed3X
#         speed7X = -speed7X
#         shield3 = False
#     if shield2:
#         fill(0, 0, 255, 190)
#         ellipse(500,500,400,400)
#     if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 212**2 and shield2:
#         print "Switch"
#         speedY = -speedY
#         speed5Y = -speed5Y
#         speed3X = -speed3X
#         speed7X = -speed7X
#         shield2 = False
#     if shield1:
#         fill(255, 0, 0, 190)
#         ellipse(500,500,200,200)
#     if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 112**2 and shield1:
#         print "Switch"
#         speedY = -speedY
#         speed5Y = -speed5Y
#         speed3X = -speed3X
#         speed7X = -speed7X
#         shield1 = False
      
>>>>>>> 8a4c7382b165ca61925cef3c54ca81d014258d0e
    
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
            Gn.play()
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
            
        ### RESULTS ###
        
        ## IF YOU WIN
        if not redBall and not greenBall and not blueBall and not yellowBall:
            background(0)
            back.pause()
            
            
            
        ## IF YOU LOSE
        if (ellipse1_y >= -50) or (ellipse5_y <= 50) or (ellipse3_x <= 50) or (ellipse7_x >= -50):
            background(255)
            back.pause()
            
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
    global explosion, pew

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
