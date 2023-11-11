def is_lucky_number(num):
    # Check if the number contains only 4 and 7
    return all(digit == '4' or digit == '7' for digit in str(num))

def lucky_numbers_between_a_and_b(a, b):
    lucky_numbers = [str(num) for num in range(a, b + 1) if is_lucky_number(num)]
    
    if not lucky_numbers:
        return -1
    else:
        return ' '.join(lucky_numbers)

# Input
a, b = map(int, input().split())

# Output
result = lucky_numbers_between_a_and_b(a, b)
print(result)
