class Lettercode():
	def __init__(self, array=[]):
		if array != []:
			self.array = array
		else:
			self.array = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '&', '%', '/', '(', ')', '=', '?', '"', ',', '.', '-', ';', ':', '_']
	def code(self, letter):
		'''
		param: letter
			type: single char of type string
		return: int from 0 to Lettercode.length()
		'''
		return self.array.index(letter)
	def decode(self, number):
		'''
		param: number
			type: int from 0 to Lettercode.length()
		return: single char
		'''
		while number >= self.length():
			number = self.length() - number
		return self.array[number]
	def length(self):
		'''
		return: self.array`s length
		'''
		return len(self.array)
