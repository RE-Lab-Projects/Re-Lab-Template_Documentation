"""
DocString Example class. Use this to describe this class.
"""

def exponentiate(base: int, exponent: int):
	"""
	Calculates an exponentiation.

	Returns
	-------
	result : int
		Exponentiation. The result of the calculation
	"""
	result = base
	for i in range(1, exponent):
		result = result * base
	return result

def main():
	print(exponentiate(1,1))
	print(exponentiate(1,2))
	print(exponentiate(2,1))
	print(exponentiate(2,2))
	print(exponentiate(3,3))
	print(exponentiate(10,10))
	print(exponentiate(1,0))
	print(exponentiate(2,0)) #this will be wrong

if __name__ == "__main__":
	main()