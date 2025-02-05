string = "GeekforGeeks!"
vowels = "aeiouAEIOU"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)