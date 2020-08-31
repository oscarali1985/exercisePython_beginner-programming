import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    recamara = spin_chamber()

    if recamara == bullet_position:
        mensaje = "You are dead!"
    else:
        mensaje= "Keep playing!"

    return mensaje





print(fire_gun())