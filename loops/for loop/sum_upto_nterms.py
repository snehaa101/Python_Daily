#----------------------------------------------------
# Topic: PYTHON LOOPS (for loop)
# Problem:Print total upto n terms
# ---------------------------------------------------

# Take input from user
n=int(input("Enter a number:"))
#initialize variable to store the total in each cycle 
total=0
# loop from 1 to n
for i in range(1,n+1): 
    total =total + i # add current number to total

# final result (out of the loop ["cause done that silly  mistake"])
print (f"The total of {n} numbers is {total}")