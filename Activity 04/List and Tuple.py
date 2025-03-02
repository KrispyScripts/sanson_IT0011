students = []

while True:
    print("\n[Record Management Program]")
    print("1. Open File")
    print("2. Save File")
    print("3. Show All Records")
    print("4. Order by Last Name")
    print("5. Order by Grade")
    print("6. Show Student Record")
    print("7. Add Record")
    print("8. Edit Record")
    print("9. Delete Record")
    print("10. Exit")
    c = input("Enter choice (1-10): ")

    if c == '1':
        f = input("Enter filename: ")
        with open(f, 'r') as file:
            students = [(
                int(row[0]),
                (row[1], row[2]), 
                float(row[3]),
                float(row[4])
            ) for row in csv.reader(file)]
        print("File opened.")

    elif c == '2':
        f = input("Enter filename: ")
        with open(f, 'w', newline='') as file:
            writer = csv.writer(file)
            for s in students:
                writer.writerow([s[0], s[1][0], s[1][1], s[2], s[3]])
        print("File saved.")

    elif c == '3':
        for s in students:
            print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}, Class: {s[2]}, Exam: {s[3]}")

    elif c == '4':
        for s in sorted(students, key=lambda x: x[1][1]):
            print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}")

    elif c == '5':
        for s in sorted(students, key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True):
            print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}, Grade: {0.6 * s[2] + 0.4 * s[3]:.2f}")

    elif c == '6':
        i = int(input("Enter ID: "))
        for s in students:
            if s[0] == i:
                print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}, Class: {s[2]}, Exam: {s[3]}")
                break

    elif c == '7':
        i = int(input("Enter ID: "))
        f = input("Enter First Name: ")
        l = input("Enter Last Name: ")
        cs = float(input("Enter Class Standing: "))
        me = float(input("Enter Exam Grade: "))
        students.append((i, (f, l), cs, me))
        print("Record added.")

    elif c == '8':
        i = int(input("Enter ID: "))
        for idx, s in enumerate(students):
            if s[0] == i:
                f = input(f"Enter First Name ({s[1][0]}): ") or s[1][0]
                l = input(f"Enter Last Name ({s[1][1]}): ") or s[1][1]
                cs = float(input(f"Enter Class Standing ({s[2]}): ") or s[2])
                me = float(input(f"Enter Exam Grade ({s[3]}): ") or s[3])
                students[idx] = (i, (f, l), cs, me)
                print("Record updated.")
                break

    elif c == '9':
        i = int(input("Enter ID: "))
        for idx, s in enumerate(students):
            if s[0] == i:
                students.pop(idx)
                print("Record deleted.")
                break

    elif c == '10':
        print("Exiting.")
        break

    else:
        print("Invalid choice.")