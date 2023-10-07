x = input()
print("ALPHA" if x.isalpha() else "IS DIGIT")
if x.isalpha():
    print("IS CAPITAL" if x.isupper() else "IS SMALL")
