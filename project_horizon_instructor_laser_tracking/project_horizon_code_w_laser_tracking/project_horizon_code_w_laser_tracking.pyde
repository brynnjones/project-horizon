def setup():
    size(1000, 1000)
    ## SPRITE STUFF ##
    global sShip
    global sX, sY
    global theta
    
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

def draw():
    background(0)
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
