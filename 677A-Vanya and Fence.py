#n=number of friends, h=fence height
n, h = map(int, input().split())
f = list(map(int, input().split()))#map objectt is iterable just like list so you don't have to convert it to list
c = 0
for i in f:
    if i > h:
        c += 2
    else:
        c += 1

print(c)
