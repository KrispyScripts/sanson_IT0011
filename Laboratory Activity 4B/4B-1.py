A = {"a","b","c","d","f","g"}
B = {"b","c","h","l","m","o"}
C = {"c","h","d","f","j","i","k"}

print("There are {} elements in set A and set B".format(len(A | B)))
print("There are {} elements in set B that is not part of A and C".format(len((B - C) - A)))
print("i. ", sorted(C-A))
print("ii. ", sorted((C&A)))
print("iii. ", sorted((C&B)|(A&B)))
print("iv. ", sorted((A&C)-B))
print("v. ", sorted((C&A)&B))
print("vi. ", sorted(B-(A|C)))