def function(x, y, z, w):
	return int((z == (not bool(x))) <= ((w <= (not bool(y))) and (y <= x)))

def logic():

	pass

if __name__ == '__main__':
	for x in range(2):
		for y in range(2):
			for z in range(2):
				for w in range(2):
					# if y == 0 and w == 0 and int(function(x, y, z, w)) == 0:
					print(f"x:{x} z:{z} w:{w} y:{y} | F:{int(function(x, y, z, w))}")
	pass