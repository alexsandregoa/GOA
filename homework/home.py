is_raining = False
has_umbrella = True

print(is_raining == True or has_umbrella == True)  
# One is true → Output: True
age = 20
has_id = True

print(age >= 18 and has_id == True)  
# Both are true → Output: True
print(                       )
# All possible values
values = [True, False]

print("AND table:")
for A in values:
    for B in values:
        print(A, "and", B, "=", A and B)

print("\nOR table:")
for A in values:
    for B in values:
        print(A, "or", B, "=", A or B)
print(                   )
bool
x = True
y = False

print(type(x))   # <class 'bool'>
print(type(y))   # <class 'bool'>
print(                       )
print(True or False) 
print(False or False)
print(True and True)
print(True and False)
print(False or True)
print(                                  )
# This Python script evaluates the expression `15 > 3 or 15 < 3`
# and explains each step using comments and printed output.

# Step 1: evaluate each comparison separately
left = 15 > 3   # 15 is greater than 3 -> this is True
right = 15 < 3  # 15 is less than 3 -> this is False

# Print the results of the sub-expressions so you can see how Python evaluates them
print("15 > 3 ->", left)    # prints: 15 > 3 -> True
print("15 < 3 ->", right)   # prints: 15 < 3 -> False

# Step 2: evaluate the full logical expression using `or`
# `or` returns True if at least one operand is True.
result = left or right

# Print the final result
print("15 > 3 or 15 < 3 ->", result)  # prints: 15 > 3 or 15 < 3 -> True

# Detailed reasoning (in comments):
# - 15 > 3 is True because 15 is greater than 3.
# - 15 < 3 is False because 15 is not less than 3.
# - The `or` operator yields True if either left or right (or both) is True.
#   Since the left side is True, the whole expression is True.

print(                           )
print(15 > 4 or 15 < 9 and 12 > 3 or 0 < 19)
True or False and True or True
True or False or True
True
