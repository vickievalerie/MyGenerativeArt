message = "this text is spinning"
def setup():
    global x, theta
    size(1000, 1000, P3D)
    x = 10
    theta = 0

def draw():
    global message, x, theta
    background(255)
    fill(0)
    f = createFont("Arial",round(x),True)
    textFont(f)                  # Set the font
    translate(width/2,height/2)  # Translate to the center
    rotate(theta)                # Rotate by theta
    textAlign(CENTER)            
    text(message,0,0)            
    theta += 0.04
    x+=0.5*x/100
    print(round(x))                # Increase rotation
