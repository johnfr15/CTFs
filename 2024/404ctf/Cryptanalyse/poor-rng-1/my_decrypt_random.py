import os
# from Cryptodome.Util.number import long_to_bytes

"""
Un générateur de nombres aléatoires efficace et sécurisé
"""
class MyGenerator:

	def __init__(self, key):
		self.feed = []
		self.feed = key

	# The first 2000 index are purely from the os.random 	
	def get_next_byte(self):
		number = 0

		for i in range(len(self.feed)):
			if i%2==0:
				number += pow(self.feed[i],i,2**8) + self.feed[i]*i
				number = ~number
			else:
				number ^= self.feed[i]*i+i


		number %= 2**8
		self.feed = self.feed[1:]
		self.feed.append(number)
		return number

	def get_random_bytes(self,length):
		random = b''

		for i in range(length):
			random += int.to_bytes(self.get_next_byte(), length=1, byteorder='big')

		return random


