# from itertools import product

def readFileSync(filename):
	with open(filename) as f:
		return f.readlines()

def logic():
	data = readFileSync('22_file.txt')
	gigastring = ''.join(data)

	maxLen = 0

	start, end = 0, 0
	while start != 4935109-12:
		start = gigastring.index('D', end)
		end = gigastring.index('D', start+1)
		string = gigastring[start:end+1]

		if string.count('O') <= 2:
			maxLen = len(string)

		# print(string)
	
	return maxLen

if __name__ == '__main__':
	print(logic())