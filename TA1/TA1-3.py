def scannerA(scounted):
    for num in range (1, 6):
        for spc in range (5-num):
            print(" ", end="")
        for num in range (1, num+1):
            print(num, end="")
        print()
scannerA(5)
def scannerB():
    num=1
    while num<=7:
        if num in [1, 3, 5, 6, 7]:
            print(str(num)*num)
        num+=1
scannerB()