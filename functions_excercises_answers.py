# ---------------------------------------------------------------------------------------------------------------------
# Exercise 1: Accept numbers from a user
# Write a program to accept two numbers from the user and calculate multiplication
# ---------------------------------------------------------------------------------------------------------------------

number1 = int(input("Please insert the first number:"))
number2 = int(input("Please insert the second number:"))
print(f"The multiplication of {number1} and {number2} is {(number1*number2)}")

# ---------------------------------------------------------------------------------------------------------------------
# Exercise 2: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.
# ---------------------------------------------------------------------------------------------------------------------


def print_age(name, age):
    print(f"{name} has this age {age}")


print_age("Tony", 83)

# ---------------------------------------------------------------------------------------------------------------------
# Exercise 3: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.
#
# call function with 3 arguments:
# func1(20, 40, 60)
#
# call function with 2 arguments
# func1(80, 100)
#
# Expected Output:
#
# Printing values
# 20
# 40
# 60
#
#
# Printing values
# 80
# 100
# ---------------------------------------------------------------------------------------------------------------------


def func1(*args):
    for arg in args:
        print(arg)


func1(20, 40, 60)
func1(80, 100)

# ---------------------------------------------------------------------------------------------------------------------
# Exercise 4: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate
# addition and subtraction. Also, it must return both addition and subtraction in a single return call.
#
# Given:
#
# def calculation(a, b):
#     # Your Code
#
# res = calculation(40, 10)
# print(res)
#
# Expected Output:
#
# 50, 30
# ---------------------------------------------------------------------------------------------------------------------


def calculation(a, b):
    adition = a + b
    substraction = a - b
    return adition, substraction


res = calculation(40, 10)
print(res)

# ---------------------------------------------------------------------------------------------------------------------
# Exercise 5: Create a function with default argument
# Write a program to create a function show_employee() using the following conditions.
#
#     It should accept the employee’s name and salary and display both.
#     If the salary is missing in the function call then assign default value 9000 to salary
#
# Given:
#
# showEmployee("Ben", 12000)
# showEmployee("Jessa")
#
# Expected output:
#
# Name: Ben salary: 12000
# Name: Jessa salary: 9000
# ---------------------------------------------------------------------------------------------------------------------


def showEmployee(employee, salary=9000):
    print(f"Name:  {employee} salary: {salary}")


showEmployee("Ben", 12000)
showEmployee("Jessa")
