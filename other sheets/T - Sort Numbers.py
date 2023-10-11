# Read input and split it into a list of integers
l = list(map(int, input().split()))

# Make a sorted copy of the list
sorted_l = sorted(l)

# Print the sorted list
for i in sorted_l:
    print(i)

# Print a newline for separation
print("")

# Print the original list
for i in l:
    print(i)
