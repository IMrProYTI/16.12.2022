def function(x, y, z, w):
	return int((z == (not bool(x))) <= ((w <= (not bool(y))) and (y <= x)))

def logic():

	pass

def myCount(x, y, z, w, out):
	x, y, z, w = str(x), str(y), str(z), str(w)
	return str(x + y + z + w).count(str(out))

if __name__ == '__main__':
	for x in range(2):
		for y in range(2):
			for z in range(2):
				for w in range(2):
					if int(function(x, y, z, w)) == 0 and myCount(x,y,z,w,0) >= 1:
						print(f"x:{x} z:{z} y:{y} w:{w} | F:{int(function(x, y, z, w))}")
	pass

# xzyw