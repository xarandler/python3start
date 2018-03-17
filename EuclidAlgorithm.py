
def divAlg(a, b):
    if a % b == 0:
    	return (a/b, 0)
    else:
        return (a/b,a%b)

def euclidAlgNorm(m, n):
    a = 0
    b = max(m,n)
    r = min(m,n)
    while r != 0:
    	a = b
    	b = r
    	r = a%b
    mgn = (m*n)/b
    return (b, mgn)

#print (euclidAlgNorm(24,36))

def euclidAlgRec(m, n):
	a = max(m,n)
	b = min(m,n)
	if a%b == 0:
		return b
	else:
		return (euclidAlgRec(b,a%b))

#print(euclidAlgRec(24, 36))

def euclidAlgPrint():
	m = input("Ange forsta talet:")
	n = input("Ange andra talet:")
	a = 0
	b = int(max(m,n))
	r = int(min(m,n))
	text = "Euclide Algorithm for " + str(b) +" and " + str(r) + "\n"
	while r != 0:
		a = b
		b = r
		q = a/b
		r = a%b
		text += (str(a) + " = " + str(q) + "*" + str(b) + " + " + str(r) + "\n")
	text += "\nGCD: "
	text += str(b)
	mgn = (m*n)/b
	return (b, mgn, text)
	

print(euclidAlgPrint()[2])