from math import*
def sieve(limit):
	upTo = limit + 1
	numbers = []
	for i in range(2,upTo,1):
		numbers.append(i)
	div = 1
	primes = []
	while div <= sqrt(limit):
		div = numbers[0]
		primes.append(div)
		for x in numbers:
			if x%div == 0:
				numbers.remove(x)
	primes = primes + numbers
	return primes

#Running the code
x = input("Sieve up to:")
myPrimes = sieve(int(x))
print(myPrimes)
