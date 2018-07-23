def setup():
    size(1000, 1000)
    ## CREATING THE SPRITE ##
    global sShip
    sShip  = loadImage("sShip.png") # If pulled from github directly, the image file and where the image should be accessed should be correct. If not, go to the repository and directly save the image into the correct folder
    ## END OF THE CODE FOR CREATING THE SPRITE ##
    
def draw():
    background(0)
    ## PLACEMENT OF THE SPRITE ##
    global sShip
    
    image(sShip, 450, 450, 100, 100)
    ## END OF THE CODE FOR PLACING THE SPRITE ##
    
    
    
    
    
