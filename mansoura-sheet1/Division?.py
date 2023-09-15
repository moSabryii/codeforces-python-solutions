t = int(input())
for i in range(t):
    r = int(input())
    if r >= 1900:
        print("Division 1")
    elif r >= 1600 and r <= 1899:
        print("Division 2")
    elif r >= 1400 and r <= 1599:
        print("Division 3")
    else:
        print("Division 4")
    
