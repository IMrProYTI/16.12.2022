def toBin(number):
	return bin(number)[2:]

def numSum(number):
	out = 0
	for num in str(number):
		out += int(num)
	return out

def logic(n):
	num = n
	for _ in range(3):
		numBin = toBin(num)
		numBin = numBin + str(numSum(num) % 2)
		num = int(numBin, 2)
	return num

if __name__ == '__main__':
	# myInput = int(input())
	myInput = 17
	print(logic(myInput)) # 139
	
	for x in range(1000):
		if logic(x) > 2054:
			print(x)
			break