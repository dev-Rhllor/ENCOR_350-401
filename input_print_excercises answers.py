# ---------------------------------------------------------------------------------------------------------------------
# Exercise 1: Accept numbers from a user
# Write a program to accept two numbers from the user and calculate multiplication
# ---------------------------------------------------------------------------------------------------------------------

number1 = int(input("Please insert the first number:"))
number2 = int(input("Please insert the second number:"))
print(f"The multiplication of {number1} and {number2} is {(number1*number2)}")

# ---------------------------------------------------------------------------------------------------------------------
# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Use the print() function to format the given words in the mentioned format.
# Display the ** separator between each string.
# Expected Output: # Name**Is**James
# ---------------------------------------------------------------------------------------------------------------------

print('Name', 'Is', 'James', sep='**')

# ---------------------------------------------------------------------------------------------------------------------
# Exercise 3: Convert Decimal number to octal using print() output formatting
# Given: num = 8
# Expected Output:
# The octal number of decimal number 8 is 10
# ---------------------------------------------------------------------------------------------------------------------
number = 8
print('%o' % number)
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 4: Display float number with 2 decimal places using print()
# Given: num = 458.541315
# Expected Output: 458.54
# ---------------------------------------------------------------------------------------------------------------------
