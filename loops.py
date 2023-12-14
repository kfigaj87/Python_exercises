# Exercise 1:

# Design a program that will prompt the user to enter 10 integers using a loop. The program should calculate the sum of all the numbers. If necessary, you can create additional variables to assist you in the calculations.

def exercise1():  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY TOP

    # START CODING HERE

    result = 0

    for i in range(10):
        number = int(input(f"Enter number {i + 1}: "))
        result += number

    return result  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY BOTTOM


# Call the function and print the results
result = exercise1()
print(result)

# Exercise 2:

# Design a program that prompts the user to enter 10 integers using a loop. The program should calculate the sum of only those numbers that are even. If necessary, you can create additional variables to assist you in the calculations.

# Assign the calculation code to the variable "result."


def exercise2():  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY TOP

    # START CODING HERE

    result = 0

    for i in range(10):
        number = int(input(f"Enter number {i + 1}: "))
        if (number % 2 == 0):
            result += number

    return result  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY BOTTOM


# Call the function and print the results
result = exercise2()
print(result)


# Exercise 3:

# Design a program that prompts the user to enter 10 integers using a loop. The program should calculate:

#     How many even numbers the user entered.
#     How many odd numbers the user entered.

# If necessary, you can create additional variables to assist you in the calculations.

# Assign the calculation codes for even and odd numbers to the variables:

#     "evenCount" for the count of even numbers.
#     "oddCount" for the count of odd numbers.


def exercise3():  # DO NOT CHANGE THIS, IT MUST BE AT THE VERY TOP

    # START CODING HERE

    evenCount = 0
    oddCount = 0

    for i in range(10):
        number = int(input(f"Enter number {i + 1}: "))

        if (number % 2 == 0):
            evenCount += 1
        else:
            oddCount += 1

    # DO NOT CHANGE THIS, IT MUST BE AT THE VERY BOTTOM
    return (evenCount, oddCount)


# Call the function and print the results
result = exercise3()
print(result)

# Exercise 4:

# Design a program where the user will enter any number of integers. When the user enters 0, the program should stop prompting for additional numbers. The program's task is to calculate the average of the numbers provided by the user. Remember!!! The digit 0 is not included in the statistics.

# For example:
# The user enters the following numbers: 2, 4, 6, 8, 0
# The average of the provided numbers is: 5

# If necessary, you can create additional variables to assist you in the calculations.

# Assign the calculation code to the variable "result."


def exercise4():

    total_sum = 0
    number_count = 0

    while True:
        number = int(input("Enter an integer (type 0 to finish): "))

        if number == 0:
            break

        total_sum += number
        number_count += 1

    result = total_sum / number_count if number_count > 0 else 0

    return round(result, 2),


# Call the function and print the results
result = exercise4()
print(result)
