#----------------------------------------------------
# Topic: PYTHON LOOPS (for loop)
# Problem: Check if no. is positive or negative and then print it's factorial.
#---------------------------------------------------


# Take input from user
n=int(input("Enter a number:"))

#initialize variable to store the total in each cycle 
fact = 1

# checks if no. is negative
if n<0:
    print(f"{n} is a negative number,\n hence factorial is not defined")

# checks if no. is 0
elif n==0:
    print(f"Factorial of {n} is 1")

# For positive numbers
else:
    for i in range(1,n+1):
     fact=fact * i

    print (f"The factorial of {n} is {fact}")
