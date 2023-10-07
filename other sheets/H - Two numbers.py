import math
a, b = map(int, input().split())

print(f"floor {a} / {b} = {math.floor(a/b)}")
print(f"ceil {a} / {b} = {math.ceil(a/b)}")
print(f"round {a} / {b} = {math.ceil(a/b) if a % b * 2 >= b else math.floor(a/b)}")

"""didn't use round function because it rounds to the nearest even number
(bankers' rounding) when there's a tie in Python 3.
In your case, 10 divided by 4 results in 2.5, and when rounded using 
round(), it rounds down to 2 because 2 is the nearest even number."""
