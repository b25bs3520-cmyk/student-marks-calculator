print("🎓 Student Marks Calculator")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

print("\nTotal Marks =", total)
print("Percentage =", percentage)

if percentage >= 90:
    print("Grade : A+ ⭐")
elif percentage >= 75:
    print("Grade : A")
elif percentage >= 60:
    print("Grade : B")
elif percentage >= 40:
    print("Grade : C")
else:
    print("Grade : Fail")
