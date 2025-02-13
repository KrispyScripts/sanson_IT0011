def is_palindrome(num):
    return str(num) == str(num)[::-1]

with open("numbers.txt") as file:
    for i, line in enumerate(file, 1):
        numbers = [int(x) for x in line.replace(',', ' ').split()]
        total = sum(numbers)
        status = "Palindrome" if is_palindrome(total) else "Not a palindrome"
        if total != 0:
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {status}")