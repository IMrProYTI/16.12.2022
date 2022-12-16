def logic(string):
	while string.count('00') == 0:
		string = string.replace('012', '30', 1)
		if string.count('011') != 0:
			string = string.replace('011', '20', 1)
			string = string.replace('022', '40', 1)
		else:
			string = string.replace('01', '10', 1)
			string = string.replace('02', '101', 1)
	return string


if __name__ == '__main__':
	for x in range(0, 11):
		string = '00' + '1'*x + '2'*abs(x-10) + '00'
		print(logic(string))