
import csv
import statistics

# 1. Generate dataset (AI-like)
students = [
    ["Alice", 20, "Female", "A", 85],
    ["Bob", 21, "Male", "B", 78],
    ["Charlie", None, "Male", "A", 92],
    ["David", 23, "Male", "C", None],
    ["Eva", 22, "Female", None, 88],
    ["Frank", None, "Male", "B", 76],
    ["Grace", 21, "Female", "A", 90],
    ["Hannah", 24, "Female", "B", 84],
    ["Ian", 23, "Male", "C", 79],
    ["Jane", 22, "Female", "A", None]
]

# 2. Handle missing numeric values (Age, Score)
ages = [s[1] for s in students if s[1] is not None]
scores = [s[4] for s in students if s[4] is not None]

mean_age = statistics.mean(ages)
mean_score = statistics.mean(scores)

for s in students:
    if s[1] is None:
        s[1] = round(mean_age, 2)
    if s[4] is None:
        s[4] = round(mean_score, 2)

# 3. Handle missing categorical value (Grade)
grades = [s[3] for s in students if s[3] is not None]
mode_grade = statistics.mode(grades)
for s in students:
    if s[3] is None:
        s[3] = mode_grade

# 4. One-hot encode categorical data (Gender, Grade)
# Gender: Male → 1, Female → 0
# Grade: A → (0,0), B → (1,0), C → (0,1)
processed = []
for s in students:
    name, age, gender, grade, score = s
    gender_male = 1 if gender == "Male" else 0
    grade_b = 1 if grade == "B" else 0
    grade_c = 1 if grade == "C" else 0
    processed.append([name, age, score, gender_male, grade_b, grade_c])

# 5. Save processed dataset to CSV
header = ["Name", "Age", "Score", "Gender_Male", "Grade_B", "Grade_C"]

with open("processed_students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(processed)

print("✅ Processed dataset saved as: processed_students.csv")

# Optional: Display result
for row in processed:
    print(row)