
#g is 9.8 (the gravitational constant)
GRAV_CONSTANT = 9.8

def falling_distance(seconds):
    distance = .5*GRAV_CONSTANT*(seconds**2)
    return distance