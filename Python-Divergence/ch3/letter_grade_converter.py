# 3-1 Letter Grade Converter

print("Letter Grade Converter")
num_grades = {
    'A': range(88, 101),
    'B': range(80, 88),
    'C': range(67, 80),
    'D': range(60, 67),
    'F': range(1, 60),
}

while True:
    user_grade = input("Enter numerical grade: ")
    for key, value in num_grades.items():
        if int(user_grade) in value:
            print(f"Letter grade: {key}")
            break
    choice = input("Continue? (y/n): ")
    if choice.lower() != 'y':
        break
print("Bye!")