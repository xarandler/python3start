from math import*
def myFunc(z):
	return (z**3 + 3*z**2 - 3)
	
def biSector(low, high, epsilon):
	lower = float(low)
	upper = float(high)
	m = (low+high)/2
	while (abs(myFunc(m))>epsilon):
		m = (lower+upper)/2
		print(m)
		if myFunc(m)>0:
			upper = m
		else:
			lower = m
	return m


result = biSector(0, 1, 0.00001)

