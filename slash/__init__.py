import math
import numpy as np

box = map(np.uint64, [158, 163, 200, 235, 223, 47, 250, 35, 101, 191, 5, 132, 161, 71, 142, 18, 7, 133, 176, 253, 246, 207, 117, 233, 138, 92, 74, 16, 187, 10, 91, 249, 94, 210, 80, 167, 13, 136, 202, 150, 62, 126, 160, 162, 186, 22, 108, 124, 112, 21, 232, 14, 148, 127, 218, 143, 214, 220, 39, 57, 190, 144, 159, 130, 88, 2, 154, 242, 81, 24, 111, 147, 66, 54, 238, 28, 37, 63, 45, 153, 169, 102, 208, 247, 226, 48, 79, 27, 183, 145, 184, 228, 180, 89, 56, 20, 11, 170, 40, 84, 152, 198, 55, 103, 237, 221, 178, 174, 8, 29, 90, 122, 205, 155, 12, 67, 30, 96, 243, 43, 254, 26, 44, 15, 193, 251, 59, 4, 78, 129, 137, 31, 203, 1, 219, 70, 181, 236, 157, 72, 225, 104, 194, 222, 53, 0, 241, 85, 131, 192, 6, 9, 114, 46, 248, 95, 240, 121, 128, 244, 239, 107, 19, 201, 25, 149, 116, 105, 34, 175, 76, 224, 146, 51, 139, 41, 75, 204, 52, 23, 171, 68, 196, 164, 50, 77, 245, 229, 134, 106, 252, 217, 115, 33, 188, 97, 61, 227, 86, 87, 82, 32, 166, 17, 98, 93, 60, 231, 140, 172, 125, 195, 212, 206, 73, 177, 3, 69, 58, 199, 118, 141, 209, 197, 109, 173, 123, 211, 135, 189, 151, 110, 213, 83, 38, 113, 216, 119, 179, 99, 36, 42, 120, 255, 185, 64, 168, 230, 49, 234, 165, 65, 156, 215, 182, 100])

def combine(result, current):
	result = result ^ (current)
	return result

def mix(result):
	result = (box[result & np.uint64(0xFF)]) | (box[(result >> np.uint64(8)) & np.uint64(0xFF)] << np.uint64(8)) | (box[(result >> np.uint64(16)) & np.uint64(0xFF)] << np.uint64(16)) | (box[(result >> np.uint64(24)) & np.uint64(0xFF)] << np.uint64(24)) | (box[(result >> np.uint64(32)) & np.uint64(0xFF)] << np.uint64(32)) | (box[(result >> np.uint64(40)) & np.uint64(0xFF)] << np.uint64(40)) | (box[(result >> np.uint64(48)) & np.uint64(0xFF)] << np.uint64(48)) | (box[(result >> np.uint64(56)) & np.uint64(0xFF)] << np.uint64(56))
	result = result * np.uint64(0xA78ACE24B25835F3)
	result = result ^ (result >> np.uint64(56))
	result = result * np.uint64(0xA785A2A2D742E537)
	return result

def slashInt(key):
	result = key
	result = mix(result)
	return result

def slash(key, length=8):
	data = [key & np.uint64(0xFF), (key & np.uint64(0xFF00)) >> np.uint64(8), (key & np.uint64(0xFF0000)) >> np.uint64(16), (key & np.uint64(0xFF000000)) >> np.uint64(24), (key & np.uint64(0xFF00000000)) >> np.uint64(32), (key & np.uint64(0xFF0000000000)) >> np.uint64(40), (key & np.uint64(0xFF000000000000)) >> np.uint64(48), (key & np.uint64(0xFF00000000000000)) >> np.uint64(56)]
	i = 0
	result = np.uint64(0)

	while (length >= 8):
		result = combine(result, data[i + 7] << np.uint64(56) | data[i + 6] << np.uint64(48) | data[i + 5] << np.uint64(40) | data[i + 4] << np.uint64(32) | data[i + 3] << np.uint64(24) | data[i + 2] << np.uint64(16) | data[i + 1] << np.uint64(8) | data[i])

		result = mix(result)

		i += 8
		length -= 8
		
	
	if length == 7:
		combine(result, data[i + 6] << np.uint64(48))
		combine(result, data[i + 5] << np.uint64(40))
		combine(result, data[i + 4] << np.uint64(32))
		combine(result, data[i + 3] << np.uint64(24))
		combine(result, data[i + 2] << np.uint64(16))
		combine(result, data[i + 1] << np.uint64(8))
		combine(result, data[i + 0])	
	elif length == 6:
		combine(result, data[i + 5] << np.uint64(40))
		combine(result, data[i + 4] << np.uint64(32))
		combine(result, data[i + 3] << np.uint64(24))
		combine(result, data[i + 2] << np.uint64(16))
		combine(result, data[i + 1] << np.uint64(8))
		combine(result, data[i + 0])
	elif length == 5:
		combine(result, data[i + 4] << np.uint64(32))
		combine(result, data[i + 3] << np.uint64(24))
		combine(result, data[i + 2] << np.uint64(16))
		combine(result, data[i + 1] << np.uint64(8))
		combine(result, data[i + 0])
	elif length == 4:
		combine(result, data[i + 3] << np.uint64(24))
		combine(result, data[i + 2] << np.uint64(16))
		combine(result, data[i + 1] << np.uint64(8))
		combine(result, data[i + 0])
	elif length == 3:
		combine(result, data[i + 2] << np.uint64(16))
		combine(result, data[i + 1] << np.uint64(8))
		combine(result, data[i + 0])	
	elif length == 2:
		combine(result, data[i + 1] << np.uint64(8))
		combine(result, data[i + 0])
	elif length == 1:
		combine(result, data[i + 0])
		
	result = mix(result)

	return result
	
seed = np.uint64(1)
def slashRandom():
	global seed
	seed = slash(seed)
	return seed
	
amplitude = 1
frequency = 0.0007
period = 100
noiseValues = []

def slashNoiseSeed():
	for i in range(period ** 2):
		noiseValues.append(float(slashRandom()) / float(0xFFFFFFFFFFFFFFFF))

def slashNoise2D(x, y):
	x = x * frequency
	y = y * frequency
	
	xi = int(math.floor(x))
	yi = int(math.floor(y))
	
	xp = xi % period
	yp = yi % period
	
	oa = noiseValues[xp * period + yp]
	ob = noiseValues[xp * period + (yp if yp == period - 1 else yp + 1)]
	oc = noiseValues[(xp if xp == period - 1 else xp + 1) * period + (yp if yp == period - 1 else yp + 1)]
	od = noiseValues[(xp if xp == period - 1 else xp + 1) * period + yp]
	
	x = x - xi
	y = y - yi
	
	oad = x * x * x * (x * (x * (6 * od - 6 * oa) + (15 * oa - 15 * od)) + (10 * od - 10 * oa)) + oa
	obc = x * x * x * (x * (x * (6 * oc - 6 * ob) + (15 * ob - 15 * oc)) + (10 * oc - 10 * ob)) + ob
	
	return (y * y * y * (y * (y * (6 * obc - 6 * oad) + (15 * oad - 15 * obc)) + (10 * obc - 10 * oad)) + oad) * amplitude