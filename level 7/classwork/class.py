# Ask the user to enter a number
num = float(input("Enter a number: "))

# Check both conditions
condition1 = num > 15
condition2 = (5 - num) > 12

# Print results
print("Number > 15:", condition1)
print("5 - Number > 12:", condition2)

# Check if both conditions are true at the same time
if condition1 and condition2:
    print("Both conditions are TRUE")
else:
    print("One or both conditions are FALSE")
print(                       )
# Ask for user input
name = input("Enter your name: ")
number = int(input("Enter a number: "))

# Check the conditions
condition1 = (name == "ana")
condition2 = (number == 50)

# Print the results
print("Name == 'ana':", condition1)
print("Number == 50:", condition2)

# Check if BOTH are true
if condition1 and condition2:
    print("Both conditions are TRUE")
else:
    print("One or both conditions are FALSE")
    