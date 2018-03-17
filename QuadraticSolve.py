from math import*

def solveQuad(a,b,c):
	x1 = 0.0
	x2 = 0.0
	d = (b**2 - 4*a*c)
	#2 real solutions
	if d > 0:
		x1 = (-b + sqrt(d))/(2*a)
		x2 = (-b - sqrt(d))/(2*a)
		return ("x1 = " + str(x1) + "\nx2 = " + str(x2))
	elif d == 0:
		x1 = (-b)/(2*a)
		return ("x1 & x2 = " + str(x1))
	else:
		Re = (-b)/(2*a)
		Im = sqrt(-d)/(2*a)
		return ("x1 = " + str(Re) + " + " + str(Im) + "i\nx2 = " + str(Re) + " - " + str(Im) + "i")


def solver():
	solve = True
	print("Ange koefficienter i ekvationen a*x^2 + bx + c = 0, sa loser jag ;)")
	while solve:
		a = input("a = ")
		b = input("b = ")
		c = input("c = ")
		result = solveQuad(a,b,c)
		print(result)
		state = raw_input("Ny ekvation? j/n")
		if state == "j":
			solve = True
		else:
			solve = False
			
solver()