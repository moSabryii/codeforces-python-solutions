# Input: Number of days
n = int(input())

# Calculate years
years = n // 365

# Calculate remaining days after subtracting years
remaining_days = n - (years * 365)

# Calculate months
months = remaining_days // 30

# Calculate remaining days after subtracting months
days = remaining_days - (months * 30)

# Output the result with meaningful labels
print(f"{years} years\n{months} months\n{days} days")

