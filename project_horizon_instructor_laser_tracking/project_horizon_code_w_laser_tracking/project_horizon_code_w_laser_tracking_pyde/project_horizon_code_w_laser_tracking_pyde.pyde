def setup():
    size(1000, 1000)
    #background
    img = loadImage('stars_in_the_night_sky_by_demykins.jpg') 
    
    #SHIELDS
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
    
    #BALLS
    
    #ball 1
    global ellipse1_x, ellipse1_y, speedY, ellipse1Negative
    ellipse1_x = 0
    ellipse1_y = -450
    speedY = .5
    ellipse1Negative = False
    #ball 5
    global ellipse5_x, ellipse5_y, speed5Y, ellipseNegative 
    ellipse5_x = 0
    ellipse5_y = 450
    speed5Y = .5
    #ball 3
    global ellipse3_x, ellipse3_y, speed3X, ellipseNagative 
    ellipse3_x = 450
    ellipse3_y = 0
    speed3X = .5 
    #ball 7 
    global ellipse7_x, ellipse7_y, speed7X, ellipseNagative 
    ellipse7_x = -450
    ellipse7_y = 0
    speed7X = -.5 
    
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
    
    
    global laserX, laserY, laserW, laserH
    
    laserX = 0
    laserY = -3
    laserW = 100000
    laserH = 3
    
    global ball
    global elipsex
    global elipsey
    global elipseS
    
    ball = True
    elipsex = -300
    elipsey = 0
    elipseS = 25
    
    global speed
    speed = 100
    
    global shoot
    shoot = False
    
    frameRate(100)

def get_coords(x, y):
    return (x - 500, -1 * (y - 500))

#DRAW

def draw():
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
    global elipsex
    global elipsey
    global elipseS
    
    noX = 100
    noY = tan(2 * PI - theta) * noX * -1
    
    #print 'other theta: ' + str(atan(noY/noX))
    #noX, noY = get_coords(noX, noY)
    translate(500, 500)    
    image(img,0,0)
    
    #calling the shield from setup
    global shield4_x, shield4_y, shield4
    global shield3_x, shield3_y, shield3
    global shield2_x, shield2_y, shield2
    global shield1_x, shield1_y, shield1
    #sheilds functions 
    if shield4:
        fill(247,215,9, 190)
        ellipse(0,0,800,800)
    if (((ellipse1_x - 0)**2 + (ellipse1_y - 0)**2) or ((ellipse3_x - 0)**2 + (ellipse3_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2)) < 412**2 and shield4:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield4 = False
    if shield3:
        fill(0, 255, 0, 180)
        ellipse(0,0,600,600)
    if (((ellipse1_x - 0)**2 + (ellipse1_y - 0)**2) or ((ellipse3_x - 0)**2 + (ellipse3_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2)) < 312**2 and shield3:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield3 = False
    if shield2:
        fill(0, 0, 255, 190)
        ellipse(0,0,400,400)
    if (((ellipse1_x - 0)**2 + (ellipse1_y - 0)**2) or ((ellipse3_x - 0)**2 + (ellipse3_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2)) < 212**2and shield2:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield2 = False
    if shield1:
        fill(255, 0, 0, 190)
        ellipse(0,0,200,200)
    if a (((ellipse1_x - 0)**2 + (ellipse1_y - 0)**2) or ((ellipse3_x - 0)**2 + (ellipse3_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2) or ((ellipse5_x - 0)**2 + (ellipse5_y - 0)**2))< 112**2 and shield1:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield1 = False
      
    global ellipse1_x, ellipse1_y, speedY, ellipse1Negative
    global ellipse5_x, ellipse5_y, speed5Y, ellipseNegative 
    global ellipse3_x, ellipse3_y, speed3X, ellipseNagative 
    global ellipse7_x, ellipse7_y, speed7X, ellipseNagative 
      
    #ball 1
    # if ball 1 hit the outter circle at 500 then  bounce back... then come back down
    ellipse1_y = ellipse1_y - speedY 
    fill(255,0,0)
    ellipse(ellipse1_x, ellipse1_y,25,25)
    if ellipse1_y < -490:
        ellipseNegative = False 
        speedY = -speedY 
            
    #ball 5
    #if ball 5 hits shield 4 at 800 then bounce back...
    fill(0,255,0)
    ellipse5_y = ellipse5_y + speed5Y
    ellipse(ellipse5_x, ellipse5_y,25,25)
    if ellipse5_y > 490:

        ellipseNegative = False 
        speed5Y = -speed5Y 
    
    #ball 3
    fill(0,0,255)
    ellipse3_x = ellipse3_x + speed3X
    ellipse(ellipse3_x, ellipse3_y,25,25)
    if ellipse3_x > 490:
        ellipseNegative = False  
        speed3X = -speed3X

    print ellipse3_x, speed3X
    
    #ball 7 
    fill(247,215,9)
    ellipse7_x = ellipse7_x + speed7X
    ellipse(ellipse7_x, ellipse7_y,25,25)
    if ellipse7_x < -490:
        ellipseNegative = False 
        speed7X = -speed7X 
     

    fill(255)
    
    stroke(255, 0, 0)
    ellipse(noX, noY, 10, 10)
    # print noX, noY
    # print 2*PI - theta, tan(2 * PI - theta)
    
    if ball:
        ellipse(elipsex,elipsey,elipseS,elipseS)

        
    #translate(500, 500)
    rotate(theta)
    image(sShip, sX, sY, 100, 100)
    
    if shoot:
        fill(254)
        rect(laserX, laserY, laserW, laserH)
        
    
        

    print degrees(theta)
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
    global elipsex
    global elipsey
    global elipseS
    
    if key == "a" or key == "A":
        theta -= .01 # This is similar to saying theta = theta - 0.05
        theta = theta % TWO_PI
    if key == "d" or key == "D":
        theta+= .01 
        theta = theta % TWO_PI
    if key == " ": #laser shooting using spacebar
        shoot = True
        testx = 0
        facingLeft = theta >= PI/2 and theta <= 3*(PI/2)
        while testx <= 500:
            testy = tan(2 * PI - theta) * testx* -1
            if ((testx - elipsex)**2 + (testy - elipsey)**2) < (elipseS/2)**2 and not facingLeft: #Tests if theta is positive
                ball = False
                break
            testy = tan(2 * PI - theta) * testx
            if ((-testx - elipsex)**2 + (testy - elipsey)**2) < (elipseS/2)**2 and facingLeft: #Tests if theta is negative
                ball = False 
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
