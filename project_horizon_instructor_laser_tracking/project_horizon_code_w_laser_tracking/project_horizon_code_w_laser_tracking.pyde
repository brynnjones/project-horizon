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
    theta = 0.00
    
    global laserX, laserY, laserW, laserH
    
    laserX = 0
    laserY = 0
    laserW = 100000
    laserH = 5
    
    frameRate(100)
    
    global speed
    speed = 100
    
    global shoot
    shoot = False

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
    
    noX = 100
    noY = tan(2 * PI - theta) * noX * -1
    
    #print 'other theta: ' + str(atan(noY/noX))
    #noX, noY = get_coords(noX, noY)
    translate(500, 500)    
    fill(255)
    stroke(255, 0, 0)
    ellipse(noX, noY, 10, 10)
    print noX, noY
    print 2*PI - theta, tan(2 * PI - theta)

        
    #translate(500, 500)
    rotate(theta)
    image(sShip, sX, sY, 100, 100)
    
    if shoot:
        fill (254)
        rect(laserX, laserY, laserW, laserH)
    
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
    
    if key == "a" or key == "A":
        theta -=.05 # This is similar to saying theta = theta - 0.05
        theta = theta % TWO_PI
    if key == "d" or key == "D":
        theta+= .05 
        theta = theta % TWO_PI
    if key == " ": #laser shooting using spacebar
        shoot = True
        
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
