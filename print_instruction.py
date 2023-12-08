# Exercise 2

# Design a program in which you will create the following variables:


#      day = 15
#      month = "June"
#      year = 1950


# Using the concatenation or f-string mechanism for the text1 and text2 variables, create a syntax that will assign the following text.


# Today is June 15, 1950.


# The values in bold must come from the variables created above.
# Pay attention to the spaces in the following constructions. The text on variables must be written in exactly the same form as presented in the example.

#      For the text1 variable - use concatenation.

#      For the text2 variable - use f-string.

def exercise():  # DON'T CHANGE THIS, IT MUST BE AT THE VERY TOP

    # START CODING HERE

    day = 15
    month = "June"
    year = 1950

    # CONCATENATION
    text1 = ("Today is " + str(day) + " " + month + " " + str(year) + ".")

    # F-STRING
    text2 = (f"Today is {day} {month} {year}.")

    return (text1, text2)  # DON'T CHANGE THIS, IT MUST BE AT THE VERY BOTTOM


# Call the function and print the results
result = exercise()
print(result)
