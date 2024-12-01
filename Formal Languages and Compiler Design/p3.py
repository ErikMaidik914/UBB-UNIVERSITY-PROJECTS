# Sum of n numbers
n = int(input("Enter the number of elements: "))
total_sum = 0

# Read each element and add to the sum
for i in range(n):
    x = int(input(f"Enter number {i + 1}: "))
    total_sum += x

# Output the sum
print(total_sum)
