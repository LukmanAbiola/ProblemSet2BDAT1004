
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']

# Part (a)
part_a_words = [word.upper() for word in words]
print("Part (a) output: " , part_a_words)

# Part (b)
part_b_words = [word.lower() for word in words]
print("Part (b) output: " , part_b_words)

# Part (c)
part_c_words = [len(word) for word in words]
print("Part (c) output: " , part_c_words)

# Part (d)
part_d_words = [[word.upper(), word.lower(), len(word)] for word in words]
print("Part (d) output: " , part_d_words)

# Part (e)
part_e_words = [word for word in words if len(word) >= 4]
print("Part (e) output: " , part_e_words)
