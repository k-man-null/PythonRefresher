from Person import People

class Student(People):
	def __init__(self, n , a, dob, c, e, sid, course, mos, school):
		super().__init__(n, a , dob, c, e)
		self.sid = sid
		self.course = course
		self.modeOfStudy = mos
		self.school = school

	def print(self):
		super().print()
		print("Student ID:", self.sid, "\tCourse:", self.course)
    	print("Mode of Study: ", self.modeOfStudy, "\tSchool:", self.school)
    	print("----------------------------------------------")
