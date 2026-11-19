count = 1
total = 0

# BUG: Missing colon at the end of the while statement caused a SyntaxError. Added ':' at the end of the line.
# BUG: Using '< 5' stopped the loop at 4 instead of including 5. Changed '< 5' to '<= 5' so 5 is added to the total.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Cannot concatenate a string and an integer with '+' (TypeError). Converted 'total' to a string using str(total).
print("Sum of 1 to 5 is: " + str(total))
