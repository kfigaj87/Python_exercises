# Exercise 1

# Design a program in which the user enters any integer (using one input() statement). The program's task is to determine whether it is an even or odd number.

# Assign one of the words to the variable "result":
# even
# odd

def exercise1():  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY TOP

    # START CODING HERE
    number = int(input("Enter any integer: "))

    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"

    return result  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY BOTTOM


# Call the function and print the results
result = exercise1()
print(result)

# Exercise 2

# Design a program where the user can enter their age (using one input() statement). Based on the information provided by the user, the program should determine the person's status according to the following conditions:

# age > 0 and age < 10 - child
# age >= 10 and age < 18 - youth
# age >= 18 - adult

# Assign one of the words to the variable "result":
# - child
# - youth
# - adult


def exercise2():  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY TOP

    # START CODING HERE
    age = int(input("Enter your age: "))

    if 0 < age < 10:
        result = "child"
    elif 10 <= age < 18:
        result = "youth"
    else:
        result = "adult"

    return result  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY BOTTOM


# Call the function and print the results
result = exercise2()
print(result)


# Exercise 3

# Design a program for the "multiplication table". The program prompts the user for two integers (two input() statements). After the user provides these two numbers, the program should then ask for their product in the next step (one input() statement). Ultimately, the program's task is to determine whether the answer is correct or incorrect.

# Assign one of the words to the variable "result":
#  - correct

#  - incorrect

def exercise3():  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY TOP

    # START CODING HERE
    number1 = int(input("Enter the first integer: "))
    number2 = int(input("Enter the second integer: "))

    product = number1 * number2

    user_answer = int(
        input(f"What is the product of {number1} and {number2}? "))

    if user_answer == product:
        result = "correct"
    else:
        result = "incorrect"

    return result  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY BOTTOM


# Call the function and print the results
result = exercise3()
print(result)
