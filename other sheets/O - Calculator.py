# Read input expression
expression = input().strip()

# Initialize variables
A = ""
S = ""
B = ""

# Iterate through the characters in the expression
for char in expression:
    if char.isdigit():
        # If the character is a digit, add it to A
        A += char
    else:
        # If the character is not a digit, it's the operator S, and the remaining part is B
        S = char
        B = expression[len(A) + 1:]
        break  # Exit the loop after finding the operator

# Convert A and B to integers
A = int(A)
B = int(B)

# Perform the mathematical operation based on the operator S
if S == '+':
    result = A + B
elif S == '-':
    result = A - B
elif S == '*':
    result = A * B
elif S == '/':
    # Use integer division to ensure the result is an integer
    result = A // B

# Print the result
print(result)
