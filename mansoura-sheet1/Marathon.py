n = int(input())

for i in range(n):
    counter = 0
    a = list(map(int, input().split()))
    for i in range(1,4):
        if a[i]>a[0]: 
            counter += 1
    print(counter)

