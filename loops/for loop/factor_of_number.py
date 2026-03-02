#-------------------------------------------------------------------------
# Topic: PYTHON LOOPS (for loop)
# Problem: WAP a program to find all the factor of a number
#-------------------------------------------------------------------------

## Factor of a number is a number which divides the given number completely without leaving any remainder.

# Taking input from user
n = int(input("Enter a number: "))

# Using for loop to find factors of the number

for i in range (1,n+1):
    if n%i==0:
        print(i)

