from math import*
def myFunc(z):
	return (z**3 + 3*z**2 - 3)
	
def diffQuotient(x,h):
	return ((myFunc(x+h) - myFunc(x-h)) / (2*h))
	
def numDiffer(startH, xValue, epsilon):
	h = float(startH)
	x = float(xValue)
	oldResult = diffQuotient(x,h)
	h = h/2
	newResult = diffQuotient(x,h)
	while (abs(oldResult - newResult) > epsilon):
		h = h/2
		oldResult = newResult
		newResult = diffQuotient(x,h)
		print("h:" + str(h) + " Derivative:" + str(newResult))
	return newResult



result = numDiffer(1,2,0.0000000001)
print(result)
