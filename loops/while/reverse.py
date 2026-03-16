# --------------------------------------------------------------
# Topic: PYTHON LOOPS (while loop)
# Problem: WAP to print the reverse of the input.
# -------------------------------------------------------------

# taking the input
n = int(input("Enter a number: "))

# initializing the variable to store the last digit of the number
last_digit = 0

# initializing the variable to store the reverse of the number
rev = 0

# using while loop to reverse the number
while n > 0:

    # getting the last digit of the number
    last_digit = n % 10

    # storing the reverse of the number
    rev = rev * 10 + last_digit

    # removing the last digit from the number
    n = n // 10

# printing the reverse of the number
print("The reverse of the number is:", rev)

"""
SAMPLE OUTPUT :

Enter a number: 1234
The reverse of the number is: 4321

"""
