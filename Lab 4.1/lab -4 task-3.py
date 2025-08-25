students = {
    1: {"name": "Ashwitha", "branch": "CSE-AIML", "cgpa": 9.8},
    2: {"name": "Meghana", "branch": "CSE-DS", "cgpa": 9.8},
    3: {"name": "Shivathmika", "branch": "CSE", "cgpa": 9.5}
}

# Example: Print all student details
for student_id, info in students.items():
    print(f"Student ID: {student_id}")
    print(f"  Name: {info['name']}")
    print(f"  Branch: {info['branch']}")
    print(f"  CGPA: {info['cgpa']}\n")