# Exercise 1

# Write a program that asks the user to enter their name (one input() statement). Using the concatenation mechanism or f-string for the variable "result," create syntax that assigns the text in the following form.

# Example: Robert, welcome to the Python course.

# The bolded value must come from the variable to which the value from the input() statement is assigned. Pay attention to spaces, punctuation marks. The text on the variable must be written exactly in the same form as the example presents.

def exercise1():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    # START CODING HERE
    name = input("Enter your name:")

    result = (f"{name}, welcome to the Python course.")

    return result  # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM


# Call the function and print the results
result = exercise1()
print(result)


# Exercise 2

# Write a program that prompts the user five times to enter any integer (five input() statements). Then, design code that calculates the average of the integers provided.

# If needed, you can create additional variables to assist you in the calculations.

# Assign the calculation code to the variable named "result."

def exercise2():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    # START CODING HERE
    number1 = int(input("Enter the first integer: "))
    number2 = int(input("Enter the second integer: "))
    number3 = int(input("Enter the third integer: "))
    number4 = int(input("Enter the fourth integer: "))
    number5 = int(input("Enter the fifth integer: "))

    sum_of_numbers = number1 + number2 + number3 + number4 + number5
    average = sum_of_numbers / 5

    result = average

    return round(result, 2)  # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM


# Call the function and print the results
result = exercise2()
print(result)

# Exercise 3

# Design an interactive shop with three products, where you will calculate the total amount a customer has to pay for a given order.

# bread_price = 2.50
# juice_price = 4.80
# donut_price = 5.50

# The user will be asked about the quantity for each of the above products (three input() statements), such as:

#     How many loaves of bread do you want to buy?
#     How many bottles of juice do you want to buy?
#     How many donuts do you want to buy?

# Responses should be provided in numbers. If needed, you can create additional variables to assist you in the calculations.

# Assign the calculation code to the variable named "result."


def exercise3():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    bread = 2.50
    juice = 4.80
    donut = 5.50

    # START CODING HERE
    quantity_bread = float(input("Enter the quantity of bread:"))
    quantity_juice = float(input("Enter the quantity of juice:"))
    quantity_donuts = float(input("Enter the quantity of donuts:"))

    total_products = (bread * quantity_bread) + \
        (juice * quantity_juice) + (donut * quantity_donuts)

    result = total_products

    return round(result, 2)  # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM


# Call the function and print the results
result = exercise3()
print(result)


# Exercise 4

# Design a program that calculates a power. The user will provide the following data (two input() statements):

#     Base of the power
#     Exponent of the power (assuming non-negative integers)

# If needed, you can create additional variables to assist you in the calculations.

# Assign the calculation code to the variable named "result."

def exercise4():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    # START CODING HERE
    base = float(input("Enter the base of the power: "))
    exponent = int(
        input("Enter the exponent of the power (non-negative integer): "))

    result = base ** exponent

    return result  # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM


# Call the function and print the results
result = exercise4()
print(result)
