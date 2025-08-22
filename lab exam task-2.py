class Student:
	def __init__(self, name: str, rollno: str, marks: float) -> None:
		self.name = name
		self.rollno = rollno
		self.marks = marks

	def get_grade(self) -> str:
		m = self.marks
		if 90 <= m <= 100:
			return "A+"
		elif 75 <= m <= 89:
			return "A"
		elif 60 <= m <= 74:
			return "B"
		elif 50 <= m <= 59:
			return "C"
		elif 0 <= m < 50:
			return "Fail"
		else:
			return "Invalid"

	def display_details(self) -> None:
		print(f"Name: {self.name}")
		print(f"Roll No: {self.rollno}")
		print(f"Marks: {self.marks}")
		print(f"Grade: {self.get_grade()}")


if __name__ == "__main__":
	try:
		name = input("Enter student name: ")
		rollno = input("Enter roll number: ")
		marks = float(input("Enter marks (0-100): "))
		student = Student(name=name.strip(), rollno=rollno.strip(), marks=marks)
		student.display_details()
	except ValueError:
		print("Invalid input. Marks must be a number.")