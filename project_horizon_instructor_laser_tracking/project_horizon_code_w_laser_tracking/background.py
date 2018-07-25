def setup():
    size(1000, 1000)
    global img 
    img = loadImage('stars_in_the_night_sky_by_demykins.jpg')
    background(255)
    # global colors
    # colors = [color(247,215,9, 190), color (0, 255, 0, 190), color(255, 0, 0, 190), color(0, 0, 255, 190)]
    #ball 1
    global ellipse1_x, ellipse1_y, speedY, ellipse1Negative
    ellipse1_x = 500
    ellipse1_y = 50
    speedY = .5
    ellipse1Negative = False
    #ball 5
    global ellipse5_x, ellipse5_y, speed5Y, ellipseNegative 
    ellipse5_x = 500
    ellipse5_y = 950
    speed5Y = -.5
    #ball 3
    global ellipse3_x, ellipse3_y, speed3X, ellipseNagative 
    ellipse3_x = 950
    ellipse3_y = 500
    speed3X = -.5 
    #ball 7 
    global ellipse7_x, ellipse7_y, speed7X, ellipseNagative 
    ellipse7_x = 50
    ellipse7_y = 500
    speed7X = .5 
    #shields 
    #shield4
    global shield4_x, shield4_y, shield4
    shield4_x = 500
    shield4_y = 500
    shield4 = True 
    #shield3
    global shield3_x, shield3_y, shield3
    shield3_x = 500
    shield3_x = 500
    shield3 = True 
    #shield2
    global shield2_x, shield2_y, shield2
    shield2_x = 500
    shield2_x = 500
    shield2 = True 
    #shield1
    global shield1_x, shield1_y, shield1
    shield1_x = 500
    shield1_x = 500
    shield1 = True 
    #sprite 
    
def draw():
    background(255)
    image(img,0,0)
    fill(255)
    ellipse(500, 500,25,25) 
    #shields 
    global shield4_x, shield4_y, shield4
    global shield3_x, shield3_y, shield3
    global shield2_x, shield2_y, shield2
    global shield1_x, shield1_y, shield1
    
    # # if ball 1, 3, 5, 7 hit shiled 4 shield 4 = False and breaks...
    
    #sheilds functions 
    if shield4:
        fill(247,215,9, 190)
        ellipse(500,500,800,800)
    if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 412**2 and shield4:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield4 = False
    if shield3:
        fill(0, 255, 0, 180)
        ellipse(500,500,600,600)
    if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 312**2 and shield3:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield3 = False
    if shield2:
        fill(0, 0, 255, 190)
        ellipse(500,500,400,400)
    if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 212**2 and shield2:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield2 = False
    if shield1:
        fill(255, 0, 0, 190)
        ellipse(500,500,200,200)
    if (((ellipse1_x - 500)**2 + (ellipse1_y - 500)**2) or ((ellipse3_x - 500)**2 + (ellipse3_y - 500)**2) or ((ellipse5_x - 500)**2 + (ellipse5_y - 500)**2) or ((ellipse7_x - 500)**2 + (ellipse7_y - 500)**2)) < 112**2 and shield1:
        print "Switch"
        speedY = -speedY
        speed5Y = -speed5Y
        speed3X = -speed3X
        speed7X = -speed7X
        shield1 = False
      
    
    
    
    
