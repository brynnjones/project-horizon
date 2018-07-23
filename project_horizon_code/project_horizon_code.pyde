def setup():
    size(1000, 1000)
    ## SPRITE STUFF ##
    global sShip
    global sX, sY
    global theta
    
    sShip  = loadImage("sShip.png") # If pulled from github directly, the image file and where the image should be accessed should be correct. If not, go to the repository and directly save the image into the correct folder
    sX = 0
    sY = 0
    theta = 0.01
    
    frameRate(60)
    
def draw():
    background(0)
    global sShip
    global sX, sY
    global theta
    
    translate(width/2, height/2)
    rotate(theta)
    image(sShip, sX, sY, 100, 100)
    
    # The Goal: To rotate with A and D
    if keyPressed:
        if key == "a" or key == "A":
            theta -= 0.05 # This is similar to saying theta = theta - 0.05
        if key == "d" or key == "D":
            theta+= 0.05       
    
    
    ## END OF THE SPRITE STUFF ##

    
    
    
    
    
