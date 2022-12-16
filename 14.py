from string import digits, ascii_lowercase, ascii_uppercase

alphabet = digits + ascii_lowercase + ascii_uppercase
intAlphabet = {}
for x in range(len(alphabet)):
	intAlphabet[alphabet[x]] = x

def myInt(number, base):
	if base <= 36:
		return int(number, base)
	else:
		b = 0
		out = 0
		for n in number[::-1]:
			out += intAlphabet[n] * base**b
			b += 1
	return out


def function(x):
	return myInt(f"123{x}", 37) + myInt(f"4{x}59", 37)


if __name__ == '__main__':
	# print(int('20', 8))
	for el in alphabet:
		if function(el) % 36 == 0:
			print(function(el) / 36)