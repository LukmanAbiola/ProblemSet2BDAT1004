def collatz(x: int):

	# Base condition
	if(x == 1):
		print(x)
		return
	# Sub problems
	print(x)
	if x%2 == 0:
		# x is even
		collatz(x//2)
	else:
		# x is odd
		collatz(3*x + 1)