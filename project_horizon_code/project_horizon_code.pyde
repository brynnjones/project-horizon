def setup():
    size(1000, 1000)
    ## SPRITE STUFF ##
    global sShip
    global sX, sY
    global theta
    global laser
    sShip  = loadImage("sShip.png") # If pulled from github directly, the image file and where the image should be accessed should be correct. If not, go to the repository and directly save the image into the correct folder
    sX = 0
    sY = 0
    theta = 0.01
    global speed
    
def laser(x,y):
    rect(x,y,5,10)
    frameRate(60)
    
def draw():
    background(0)
    global sShip
    global sX, sY
    global theta
    global laser
    
    
    translate(width/2, height/2)
    rotate(theta)
    image(sShip, sX, sY, 100, 100)
    laser(47.5,5)
    # The Goal: To rotate with A and D
    if keyPressed:
        if key == "a" or key == "A":
            theta -= 0.05 # This is similar to saying theta = theta - 0.05
        if key == "d" or key == "D":
            theta+= 0.05 
        if key == " ": #laser shooting using spacebar
           speed = 100
           while speed > -20 0   :
            fill (254,254,254)
            noStroke()
            laser(47.5,speed)
            speed = speed-2
    
    ## END OF THE SPRITE STUFF ##

    
    
    
    
    
