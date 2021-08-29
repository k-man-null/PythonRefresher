class People:
	#This will be the constructor
	def __init__(self, n, a, dob, c, e ):
		self.__name = n
		self.__age = a
		self.dob = dob
		self.contact = c
		self.email = e


	#define some other methods

	def getName(self):
		return self.__name

	def setName(self, newName):
		self.__name = newName

	def getAge(self):
		return self.__age

	def setAge(self, newAge):
		if newAge > O:
			self.__age = newAge
		else:
			print("Error: Age cannot be lower than 1")

	def print(self):
		print("-------------------------------------")
		print("Name: ", self.__name, "\tDOB", self.dob)
		print("Age: ", self.__age)
		print("Contact:", self.contact)
		print("Email:", self.email)

		

