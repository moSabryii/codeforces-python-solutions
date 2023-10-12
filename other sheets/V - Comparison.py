a, s, b = input().split()

a, b = int(a), int(b)

if s == ">":
    print("Right" if a > b else "Wrong")
elif s == "<":
    print("Right" if a < b else "Wrong")
else:
    print("Right" if a == b else "Wrong")
    
    
