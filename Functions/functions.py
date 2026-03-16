# -------------------------------------------------------
# Topic: FUNCTIONS
# Description :
#          - Some important points to remember
#          - Syntax
# -------------------------------------------------------

# IMP POINTS :

# (1) A function is a block of code which only runs when it is called.
# (2) A function can return data as a result.
# (3) A function helps avoiding code repetition.
# (4) Function definitions cannot be empty.
#     If you need to create a function placeholder without any code,
#     use the pass statement

# SYNTAX :

#  a function is defined using the def keyword
# Example :


def my_function():
    print("Hello from a function")


# calling a function
my_function()

""" OUTPUT
Hello from a function
"""

# parameter = thing accepted (a,b)
# argument = thing provided to parameter (20,11)


def sum(a, b=22):  # b now has it's default value
    print(f"The sum is {a+b}")


# -----------------------------------------
# Topic : Types of Arguments
# ----------------------------------------

# KEYWORD ARGUMENT - arguments with the key = value syntax.
#                  - the order of the arguments does not matter here.
sum(a=20, b=11)

# DEFAULTL ARGUMENT - assign default values to parameters.
#                   - If the function is called without an argument,
#                      it uses the default value
sum(a=55)
# not given b since has it's default value
sum(a=50, b=5)
# even if have default fir bhi dedi then it'll replace the default one

""" OUTPUT 
The sum is 31
The sum is 77
The sum is 55
"""
