def readFileSync(filename):
	with open(filename) as f:
		return f.readlines()

def logic(data):
	counter = 0
	myMax = None

	for i in range(len(data)-1):
		couple = [str(int(data[i])), str(int(data[i+1]))]

		if min(couple)[-1] == '3':
			couple = list(map(int, couple))
			if min(couple)**2 < couple[0]**2 + couple[1]**2:
				counter += 1
				if myMax == None:
					myMax = couple[0]**2 + couple[1]**2
				else:
					if myMax < couple[0]**2 + couple[1]**2:
						myMax = couple[0]**2 + couple[1]**2

	return counter, myMax

if __name__ == '__main__':
	file = readFileSync('file_17.txt')
	print(logic(file))