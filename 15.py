def isDevide(n, m):
	return n % m == 0

def function(x, y, A):
	return (isDevide(108, x) <= (not isDevide(x, y)) or (x+y > 80) or (A-y > x))


if __name__ == '__main__':
	for i in range(50, 100):
		flag = True
		for x in range(1, 200):
			for y in range(1, 200):
				if not function(x, y, i):
					flag = False
		if flag:
			print(i)
	pass