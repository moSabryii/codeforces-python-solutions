c = int(input())
a = list(map(int, input().split()))
e = o = p = n = 0
for i in range(c):
    if a[i] % 2 == 0:
        e += 1
    else:
        o += 1
    if a[i] == 0:
        pass
    elif a[i] > 0:
        p += 1
    else:
        n += 1

print(f"Even: {e}")
print(f"Odd: {o}")
print(f"Positive: {p}")
print(f"Negative: {n}")
