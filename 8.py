from itertools import product

def logic():
	vowels = 'ОИА'
	consonants = 'ПЛН'

	counter = 0
	string = vowels + consonants
	for l in product(string, repeat=8):
		el = ''.join(l)

		cv = 0
		cc = 0
		for x in el:
			if x in vowels:
				cv += 1
			if x in consonants:
				cc += 1

		if cc > cv:
			counter += 1
		
	return counter

if __name__ == '__main__':
	print(logic())