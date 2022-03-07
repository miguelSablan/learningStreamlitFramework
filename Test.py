class COP4814Student:
	def __init__(self, first_name, last_name, panther_id, email, grade):
		self.first_name = first_name
		self.last_name = last_name
		self.panther_id = panther_id
		self.email = email
		self.grade = grade

andriusB = COP4814Student("Andrius","Bubelis",12001,"andrius@cop4814.edu",87)
danielR = COP4814Student("Daniel","Ruiz",12002,"daniel@cop4814.edu",92)

print(andriusB)
print(danielR)