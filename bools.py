"""Boolean Module, made by Jacob Kodner"""

def xor(x, y):
	"""Returns a Boolean resulting in using the XOR method on x and y.\n
	XOR is equivalent to an OR statement that returns False if both conditions are True.\n
	Examples:
	xor(0, 0) --> False
	xor(1, 0) --> True
	xor(1, 1) --> False
	"""
	return bool(x) != bool(y)

def xnor(x, y):
	"""Returns a Boolean resulting in using the XNOR method on x and y.\n
	XNOR is the negated form of the XOR statement.\n
	Examples:
	xnor(0, 0) --> True
	xnor(1, 0) --> False
	xnor(1, 1) --> True
	"""
	return bool(x) == bool(y)

def nand(x, y):
	"""Returns a Boolean resulting in using the NAND method on x and y.\n
	NAND is the negated form of the AND statement.\n
	Examples:
	nand(0, 0) --> True
	nand(1, 0) --> True
	nand(1, 1) --> False
	"""
	return not (x and y)

def nor(x, y):
	"""Returns a Boolean resulting in using the NOR method on x and y.\n
	NOR is the negated form of the OR statement.\n
	Examples:
	nor(0, 0) --> True
	nor(1, 0) --> False
	nor(1, 1) --> False
	"""
	return not (x or y)

def truify(*objects):
	"""Takes in 1 or more objects and returns a modified version of said object by making it's
	overall boolean value True. If there is more than one object, a list of objects is returned\n
	Acceptable Input Types: str, tuple, list, dict, set, buffer, bool, NoneType, xrange, bytearray,
	int, float, long, and complex.
	"""
	objs = []
	if len(objects) != 0:
		for x in objects:
			if isinstance(x, str):
				obj = " "
			elif isinstance(x, tuple):
				obj = (True)
			elif isinstance(x, list):
				x.append(True)
				obj = x
			elif isinstance(x, dict):
				obj = {True: True}
			elif isinstance(x, set):
				obj = {True}
			elif isinstance(x, buffer):
				obj = buffer(" ")
			elif isinstance(x, (bool, type(None))):
				obj = True
			elif isinstance(x, xrange):
				obj = xrange(1)
			elif isinstance(x, bytearray):
				obj = bytearray(" ")
			elif isinstance(x, int):
				obj = 1
			elif isinstance(x, float):
				obj = 1.0
			elif isinstance(x, long):
				obj = 1L
			elif isinstance(x, complex):
				obj = 1j
			objs.append(obj)
	elif len(objects) == 0:
		return True
	if len(objects) == 1:
		objs = objs[0]
	return objs

def falsify(*objects):
	"""Takes in 1 or more objects and returns a modified version of said object by making it's
	overall boolean value False. If there is more than one object, a list of objects is returned\n
	Acceptable Input Types: str, tuple, list, dict, set, buffer, bool, NoneType, xrange, bytearray,
	int, float, long, and complex.
	"""
	objs = []
	if len(objects) != 0:
		for x in objects:
			if isinstance(x, str):
				obj = ""
			elif isinstance(x, tuple):
				obj = ()
			elif isinstance(x, list):
				obj = []
			elif isinstance(x, dict):
				obj = {}
			elif isinstance(x, set):
				obj = {}
			elif isinstance(x, buffer):
				obj = buffer("")
			elif isinstance(x, (bool, type(None))):
				obj = False
			elif isinstance(x, xrange):
				obj = xrange(0)
			elif isinstance(x, bytearray):
				obj = bytearray("")
			elif isinstance(x, int):
				obj = 0
			elif isinstance(x, float):
				obj = 0.0
			elif isinstance(x, long):
				obj = 0L
			elif isinstance(x, complex):
				obj = 0j
			objs.append(obj)
	elif len(objects) == 0:
		return True
	if len(objects) == 1:
		objs = objs[0]
	return objs