sample = input("Enter Digits: ")
def scanner(scounted):
    digits = 0
    for char in scounted:
        if char.isdigit():
            digits+=int(char)
    print("Sum of Digits: "+str(digits))
scanner(sample)