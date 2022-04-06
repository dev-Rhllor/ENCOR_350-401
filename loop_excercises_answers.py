# ---------------------------------------------------------------------------------------------------------------------
# Exercise 1: Print First 10 natural numbers using while loop
# Expected output:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ---------------------------------------------------------------------------------------------------------------------

number = 1
while number <= 10:
    print(number)
    number = number + 1


# ---------------------------------------------------------------------------------------------------------------------
# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.
#
# 1
# 1 2
# 1 2 2
# 1 2 3 4
# 1 2 3 4 5
# ---------------------------------------------------------------------------------------------------------------------

counter = 1
list_number = []

while counter <= 5:
    list_number.append(counter)
    for numbers in list_number:
        print(numbers, end=" ")
    print("")
    counter = counter + 1

# ---------------------------------------------------------------------------------------------------------------------
# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
#
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
#
# Expected Output:
#
# Enter number 10
# Sum is:  55
# ---------------------------------------------------------------------------------------------------------------------

number = int(input("Enter number: "))

total = 0

while number > 0:
    total = total + number
    number = number - 1
else:
    print(f"Sum is: {total}")


# ---------------------------------------------------------------------------------------------------------------------
# Exercise 4:  Write a program to accept a word from a user and print each letter in a new line.
#
# For example, word = serendipity
#
# s
# e
# r
# e
# n
# d
# i
# p
# i
# y
# ---------------------------------------------------------------------------------------------------------------------

word = input("Enter word: ")
for letter in word:
    print(letter)
