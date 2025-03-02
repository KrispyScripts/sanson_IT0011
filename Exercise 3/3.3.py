lname = input("Enter your last name: ")
fname = input("Enter your first name: ")
age = input("Enter your age: ")
conum = input("Enter contact number: ")
cor = input("Enter course: ")

info=f"Last Name: {lname}\nFirst Name: {fname}\nAge: {age}\nContact Number: {conum}\nCourse: {cor}\n"

with open("Exercise 3/students.txt", "w") as f:
    f.write(info)

print ("Student information has been saved to 'students.txt'")
