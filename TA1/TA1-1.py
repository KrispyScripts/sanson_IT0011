sample = input("Enter String: ")
def scanner(scounted):
    vowels="aeiouAEIOU"
    vcount=0
    consonants="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    ccount=0
    scount=0
    ncount=0
    for char in scounted:
        if char in vowels:
            vcount +=1
        elif char in consonants:
            ccount +=1
        elif char.isspace():
            scount +=1
        else:
            ncount+=1
    print("Vowels: "+str(vcount).rjust(15))
    print("Consonants: "+str(ccount).rjust(11))
    print("Spaces: "+str(scount).rjust(15))
    print("Other Characters: "+str(ncount).rjust(5))
scanner(sample)
