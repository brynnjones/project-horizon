def setup():
    size(1000, 1000)
    
    #SPRITES
    global northShip, southShip, eastShip, westShip
    global north, south, east, west
    global sX, sY, sW, sH
    
    northShip = loadImage("sShip_North.png")
    southShip = loadImage("sShip_South.png")
    eastShip = loadImage("sShip_East.png")
    westShip = loadImage("sShip_West.png")
    
    north = True
    south = False
    east = False
    west = False
    
    sX = 450
    sY = 450
    sW = 95
    sH = 95
    
    
def draw():
    background(0)
    global northShip, southShip, eastShip, westShip
    global north, south, east, west
    global sX, sY, sW, sH
    
    if north:
        image(northShip, sX, sY, sW, sH)
    if south:
        image(southShip, sX, sY, sW, sH)
    if east:
        image(eastShip, sX, sY, sW, sH)
    if west:
        image(westShip, sX, sY, sW, sH)
        
    if keyPressed:
        if key == "W" or key == "w":
            north = True
            south = False
            east = False
            west = False
        if key == "S" or key == "s":
            north = False
            south = True
            east = False
            west = False
        if key == "D" or key == "d":
            north = False
            south = False
            east = True
            west = False
        if key == "A" or key == "a":
            north = False
            south = False
            east = False
            west = True
            
            
 
    
    laserW = 5
    laserH = 60
    
    shooter = False
    
    rect(laserX, laserY, laserW, laserH)
    
    if key == " ":
        shooter = True
