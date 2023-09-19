n = int(input())
counter = 0
for i in range(13,n+1):
    if i%13==0:
        counter += 1
        if counter > 0:
            break;

if counter > 0:
    print("YES")
else:
    print("NO")
