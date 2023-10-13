a, s, b, q, c = input().split()
a, b, c = int(a), int(b), int(c)

if s == "+":
    result = a + b
elif s == "-":
    result = a - b
else:
    result = a * b

if result == c:
    print("Yes")
else:
    print(result)
