# --------------------------------------------------------------
# Topic: PYTHON LOOPS (while loop)
# Problem: WAP to check if the input is a palindrome or not.
# -------------------------------------------------------------

# taking the input
n = int(input("Enter a number: "))

# initializing the variable to store the reverse of the number
rev = 0

# using while loop to reverse the number
while n > 0:

    # storing the reverse of the number
    rev = rev * 10 + n % 10

    # removing the last digit from the number
    n = n // 10

# printing the reverse of the number
print("The reverse of the number is:", rev)

# checking if the number is a palindrome or not
if n == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
