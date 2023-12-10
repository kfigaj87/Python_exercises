# Exercise 1

# Design a program in which you create the following variables:

# number1 = 5
# number2 = 10

# Perform the appropriate arithmetic operations for the given variables:

# sum =
# difference =
# product =
# quotient =
# modulo =

def exercise1():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    # START CODING HERE

    number1 = 5
    number2 = 10

    sum_result = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    modulo = number1 % number2

    # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM
    return (sum_result, difference, product, quotient, modulo)


# Call the function and print the results
result = exercise1()
print(result)

# Exercise 2

# Design the appropriate code that will calculate the value for the following task. If needed, you can create additional variables to assist you in the calculations.

# A car consumes 8 liters of fuel per 100 kilometers. How much fuel will it consume after traveling 488 kilometers?

# Assign the calculation code to the variable named "result."


def exercise2():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    # START CODING HERE
    distance = 488
    fuel_consumption = 8

    result = (distance / 100) * fuel_consumption

    return round(result, 2)  # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM


# Call the function and print the results
result = exercise2()
print(result)

# Exercise 3

# Design the appropriate code that will calculate values for the following tasks. If needed, you can create additional variables to assist you in the calculations.

#     Area of a square with a side length of 5.
#     Perimeter of a triangle with side lengths of 3, 4, and 6.
#     Area of a circle with a radius of 3.
#     Area of a triangle with a height of 7 and a base length of 15.

# Assign the calculation code to the following variables:
# squareArea
# trianglePerimeter
# circleArea
# triangleArea


def exercise3():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    # START CODING HERE
    square_side = 5

    side1 = 3
    side2 = 4
    side3 = 6

    circle_radius = 3

    triangle_height = 7
    triangle_base = 15

    squareArea = square_side ** 2
    trianglePerimeter = side1 + side2 + side3
    circleArea = 3.14 * circle_radius ** 2
    triangleArea = 0.5 * triangle_base * triangle_height

    # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM
    return (round(squareArea, 2), round(trianglePerimeter, 2), round(circleArea, 2), round(triangleArea, 2))


# Call the function and print the results
result = exercise3()
print(result)

# Exercise 4

# Write a program that calculates the total cost of products for a specific order. If needed, you can create additional variables to assist you in the calculations.

# Product prices:

#     Bread (1.99 PLN per 1 unit)
#     Milk (2.50 PLN per 1 liter)
#     Juice (6.45 PLN per 1 liter)
#     Candies (10.25 PLN per 1 kg)

# The order is as follows:

#     5 units of bread
#     0.5 liters of milk
#     7 liters of juice
#     5 kg of candies

# Assign the calculation code to the variable named "result."


def exercise4():  # DO NOT CHANGE THIS, IT MUST BE AT THE TOP

    # START CODING HERE
    bread_price = 1.99
    milk_price = 2.50
    juice_price = 6.45
    candies_price = 10.25

    bread_quantity = 5
    milk_quantity = 0.5
    juice_quantity = 7
    candies_quantity = 5

    bread_cost = bread_quantity * bread_price
    milk_cost = milk_quantity * milk_price
    juice_cost = juice_quantity * juice_price
    candies_cost = candies_quantity * candies_price

    result = bread_cost + milk_cost + juice_cost + candies_cost

    return round(result, 2)  # DO NOT CHANGE THIS, IT MUST BE AT THE BOTTOM


# Call the function and print the results
result = exercise4()
print(result)
