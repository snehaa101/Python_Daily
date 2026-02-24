#----------------------------------------------------
# Topic: PYTHON LOOPS
# Problem: Sum upto n terms
# ---------------------------------------------------

# Take input from user
n=int(input("Enter a number:"))

for i in range(1,n+1): 
    sum = sum + i
    print (f"The sum of {n} numbers is {sum}")