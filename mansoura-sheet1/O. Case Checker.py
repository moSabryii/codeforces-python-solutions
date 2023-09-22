n = int(input())
s = input()
for i in s:
    if i.isupper():
        print("is upper")
    elif i.islower():
        print("is lower")
    else:
        print("is digit")
