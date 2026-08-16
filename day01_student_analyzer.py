student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))

while True:

    subject_1 = int(input("Enter marks in Python (0-100): "))
    subject_2 = int(input("Enter marks in Mathematics (0-100): "))
    subject_3 = int(input("Enter marks in DBMS (0-100): "))
    subject_4 = int(input("Enter marks in Computer Networks (0-100): "))
    subject_5 = int(input("Enter marks in DSA (0-100): "))

    if (0 <= subject_1 <= 100 and
        0 <= subject_2 <= 100 and
        0 <= subject_3 <= 100 and
        0 <= subject_4 <= 100 and
        0 <= subject_5 <= 100):

        break

    print("Invalid marks! All marks must be between 0 and 100.")

Total = subject_1+subject_2+subject_3+subject_4+subject_5

percentage = Total / 500 * 100

result = ""

if percentage>40:
    result="Pass"
else:
    result="fail"

grade = ""
if percentage>=90:
    grade = "A+"
elif percentage >=80:
     grade = "A"
elif percentage >=70:
    grade = "B+"
elif percentage >=60:
    grade = "B"
elif percentage>=50:
    grade = "C"
elif percentage>=40:
    grade = "D"
else:
    grade = "F"

print("="*30)
print("STUDENT PERFORMANCE REPORT")
print("="*30)

print("\nName:",student_name)
print("Age:",student_age)

print("\nPython:",subject_1)
print("Mathemetics:",subject_2)
print("DBMS:",subject_3)
print("Networks:",subject_4)
print("DSA:",subject_5)

print(f"\nTotal:{Total}/500")
print("Percentage:",percentage)
print("Result:",result)
print("Grade:",grade)

print("="*30)





