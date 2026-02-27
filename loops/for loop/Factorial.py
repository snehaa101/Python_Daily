#----------------------------------------------------
# Topic: PYTHON LOOPS (for loop)
# Problem: 1.Print factorial of a number.
#---------------------------------------------------
# Take input from user
n=int(input("Enter a number:"))

#initialize variable to store the total in each cycle 
fact= 1 # **NEVER INTIALIZE FROM 0 IN case of multipication**

# loop from 1 to n
for i in range(1,n+1):
    fact=fact * i

print (f"The factorial of {n} is {fact}")

