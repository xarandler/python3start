def fibonacciList():
    a1 = input("Ange a1:")
    a2 = input("Ange a2:")
    limit = input("Ange ovre grans:")
    a = int(a1)
    b = int(a2)
    fib = (a + b)
    result = "Fibonaccinumbers below " + str(limit) + ": " + str(a) + ", " + str(b)
    while fib < limit:
        result += ", " + str(fib)
        a = b
        b = fib
        fib = a + b
    return result

#print(fibonacciList())

fibNumbers = [1,1]

def fibbeRec(n):
	result = 0
	if int(n) <= 0:
		return 0
	elif (n == 1 or n == 2):
		return 1
	else:
		result = fibbeRec(n-1) + fibbeRec(n-2)
		if result > fibNumbers[-1]:
			fibNumbers.append(result)
		return result


def fibbeArray():
    limit = int(input("Ange antal Fibonaccital du vill ha:"))
    return (fibbeRec(limit), fibNumbers)

print(fibbeArray()[1])
