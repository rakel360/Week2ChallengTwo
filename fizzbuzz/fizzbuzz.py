
def fizzbuzz(a, b):
	try:
		if (len(a)+len(b))%3==0 and (len(a)+len(b))%5==0:
			return "fizzbuzz"
		elif (len(a)+len(b))%3==0:
			return "fizz"
		elif (len(a)+len(b))%5==0:
			return "buzz"
		else:
			return len(a)+len(b)

	except TypeError:
		return "Invalid input"




