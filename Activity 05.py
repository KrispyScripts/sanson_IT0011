def divide():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return None
    if denominator == 0:
        print("Division by zero is not allowed.")
        return None
    quotient = numerator/denominator
    print("\nThe quotient is: ", quotient)
    return quotient

def exponent():
    try:
        base = float(input("Enter the base: "))
        power = float(input("Enter the power: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return None
    result = base ** power
    print("\nThe result is: ", result)
    return result

def remain():
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return None
    if divisor == 0:
        print("Division by zero is not allowed.")
        return None
    remainder = dividend % divisor
    print("\nThe remainder is: ", remainder)
    return remainder

def summ():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number (must be higher): "))
    except ValueError:
        print("Error: Invalid input. Please enter integers.")
        return None
    if num2 <= num1:
        print("Second number must be higher than the first number")
        return None
    total = sum(range(num1, num2 + 1))
    print("\nThe total is: ", total)
    return total

def menu():
    options = ('D','d','X','x','F','f','R','r','E','e')

    while True:
        print("\n+-Mathematical Functions-+")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")
        select = input("Enter the letter of the function you wish to use: ")
        if select in options:
            return select
        else:
            print("\nOption Not Found.")

while True:
    select = menu()
    if select in ('D', 'd'):
        divide()
    elif select in ('E', 'e'):
        exponent()
    elif select in ('R', 'r'):
        remain()
    elif select in ('F', 'f'):
        summ()
    elif select in ('X', 'x'):
        exit()








