def F(n):
	if n == 0:
		return 0
	else:
		return F(n // 10) + (n // 10)


if __name__ == '__main__':
	counter = 0
	for i in range(237567892, 1134567009+1):
		if F(i) > F(i + 1):
			counter += 1
	print(counter)