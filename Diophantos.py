from math import*
def returnBlanks(length):
	blanks = ""
	if length > 0:
		for i in range(1,(length),1):
			blanks += " "
	return blanks

def returnSign(powerOfNeg):
	return "+" if (powerOfNeg % 2 == 0) else "-"

def getLength(nr):
	return int(log10(int(nr)) + 1)

def maxLength(array):
	mx = max(array)
	length = getLength(mx)
	return int(length)


def bhaskara(m, n, rightSide):
    #Checking all is positive
	if m < 1 or n < 1 or rightSide < 1 :
		return "Use only positive integers, if you have a problem involving negative signs, rewrite the problem substituting for instance:\n\nz = (-x)\n\nThen solve the problem and change signs for the solution of x"
    #Checking if xCoeff is smallest, we have to remeber this in the end
	swapped = False
	if m > n:
		swapped = True
	a = 0
	b = max(n,m)
	r = min(n,m)
	q = 0
	rs = rightSide
    #Creating array for the quotients in Euclide
	quotients = []
    #Creating array for the solutions in Bhaskara, adding the first "empty" solution.
	solutions = [0]
    #Creating a text-container and adding basic stuff
	text = "Solving Diophanic Equation " + str(m) + "x + " + str(n) + "y = " + str(rightSide) + "\n\n"
	text += "Euclide Algoritm for " + str(b) + " and " + str(r)
	text += "\n===============================\n"
    #Creating som helper variables for the max length of quotients and solutions
	numCharsQuotient = 0
	numCharsSolutions = 0
    #Variables holding the final particular solutions
	x = 0
	y = 0
    #Performing Euclide
	while r != 0:
		a = b
		b = r
		q = int(a/b)
		r = a % b
		text += str(a) + " = " + str(q) + "*" + str(b) + " + " + str(r) + "\n"
        #Saving the quotients for later
		quotients.insert(0, q)
	text += "\n===============================\n"
    #Saving gcd
	gcd = b
    #Checking if the equation is solvable
	if rs % b != 0:
		text += "No solution because gcd = " + str(b) + "does not divide rightside = " + str(rs)
		text += "\n===============================\n"
		return text

    #Simplifying the equation
	a = int(m / gcd)
	b = int(n / gcd)
	rs = int(rs / gcd)
    #If any or both of the coefficients is 1, we give the simple solution
	if a == 1:
		if b == 1:
			text += "\nSolution for reduced equation where n in N:\n"
			text += "\n==============================="
			text += "x + y = " + str(rs)
			text += "\n===============================\n"
			text += "x = " + str(rs) + " + n\n"
			text += "y = 0 - n"
			text += "\n==============================="
		else:
			text += "\nSolution for reduced equation where n in N:\n"
			text += "\n===============================\n"
			text += "x + " + str(b) + "y = " + str(rs)
			text += "\n===============================\n"
			text += "x = " + str(rs) + " + " + str(b) + "n\n"
			text += "y = 0 - n"
			text += "\n==============================="
		return text

	if b == 1:
		text += "\nSolution for reduced equation where n in N:\n"
		text += "\n==============================="
		text += str(a) + "x + y = " + str(rs)
		text += "\n==============================="
		text += "x = 0 + n\n"
		text += "y = " + str(rs) + " - " + str(a) + "n\n"
		return text
    #Starting the Bhaskara schema with som text
	text += "\nBhaskara for reduced equation:\n"
	text += "===============================\n"
	text += str(a) + "x + " + str(b) + "y = " + str(rs)
	text += "\n-------------------------------\n"
    #Adding the rightside as the first "quote". Compare with the schema
	quotients[0] = rs
    #Moving the rightside to the place of the first solution
	solutions.append(rs)
    #Stepping through bhaskaras schema, adding the solutions to the array for the solutions
	for i in range(2, len(quotients)+1, 1):
		solutions.append(solutions[i-1] * quotients[i-1] + solutions[i-2])
    #Reversing both arrays to enable printing
	solutions.reverse()
	quotients.reverse()
    #Checking the max length of quotients and solutions to improve printing
	numCharsQuotient = maxLength(quotients)
	numCharsSolutions = maxLength(solutions)
    #Printing Bhaskaras schema
	for i in range(0, len(quotients), 1):
		text += str(quotients[i]) + returnBlanks(numCharsQuotient-getLength(quotients[i])) + " |"
		text += str(solutions[i]) + returnBlanks(numCharsSolutions-getLength(solutions[i])) + " |"
		text += " " + str(returnSign(i)) + "\n"
    #Checking if we swapped places in the beginning to know which solution that belongs to which varaible.
	if swapped:
		x = (-1)**(len(quotients)-2) * solutions[1]
		y = (-1)**(len(quotients)-1) * solutions[0]
	else:
		y = (-1)**(len(quotients)-2) * solutions[1]
		x = (-1)**(len(quotients)-1) * solutions[0]
    #Finnishing it all off and printing the solution
	text += "==============================="
	text += "\n\nGeneral solution where n in N"
	text += "\n==============================="
	text += "\nx = " + str(x) + " + " + str(b) + "n\n"
	text += "y = " + str(y) + " - " + str(a) + "n"
	text += "\n===============================\n\n"
    #Returning the textflow
	return (text)

first = int(input("Ange x-koeff"))
second = int(input("Ange y-koeff"))
rhs = int(input("Ange hogerled"))
test = bhaskara(first, second, rhs)
print(test)
