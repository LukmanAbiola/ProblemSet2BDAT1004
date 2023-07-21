def binary(num: int):
	if num < 0:
		print("Provide a non-negative number")
		return
	if num == 0:
		return "0"

	binary_out = ""
	last_bit = num % 2

	# get remaining representation
	sub_binary_out = ""
	if num // 2 != 0:
		# to avoid printing 0 twice, since the base case handles num == 0
		sub_binary_out = binary(num//2)
	binary_out = sub_binary_out + str(last_bit)
	
	return binary_out