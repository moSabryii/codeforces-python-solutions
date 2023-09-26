n = int(input())

if n > 1:
    # Iterate from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number between 2 and the square root of n, it is not prime
        if (n % i) == 0:
            print("NO")
            break
    else:
        # If the loop completes without finding a divisor, n is prime
        print("YES")
else:
    # Numbers less than or equal to 1 are not prime
    print("NO")
