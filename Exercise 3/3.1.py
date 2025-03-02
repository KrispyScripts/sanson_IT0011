finame = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")
funame = finame + " " +lname
sname = funame[0:3]

print ("Full Name: {}".format(funame))
print ("Sliced name: {}".format(sname))
print ("Greeting message: Hello, {}! Welcome. You are {} years old.".format(sname, age))