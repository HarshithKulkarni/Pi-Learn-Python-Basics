class example:

	def __init__(self):
		
		self.__hidden_variable = 0
		self.normal_variable = 0

	def add(self,var):

		self.__hidden_variable += var
		# self.__hidden_variable = self.__hidden_variable + var

		self.normal_variable += var
		print(f"This is Hidden {self.__hidden_variable}")
		print(f"This is Normal {self.normal_variable}")

if __name__ == '__main__':
	
	obj = example()
	obj.add(2)
	print(f"This is printing Normal Variable : {obj.normal_variable}")
	print(f"This is printing Hidden Variable : {obj.__hidden_variable}")