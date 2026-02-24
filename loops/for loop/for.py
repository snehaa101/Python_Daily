#-------------------------------------------------------
# Topic : Python Loops (FOR LOOP)
# Description :
#          - Some important points to remember
#          - Syntax
#          - Simple examples of using basic FOR loop 
#-------------------------------------------------------

###-----IMP POINTS----###

#1# A for loop is used for iterating over a sequence 
#    (that is either a list, a tuple, a dictionary, a set, or a string).

#2# With the for loop we can execute a set of statements, 
#    once for each item in a list, tuple, set etc.

#3# range(start, stop, step)

#-------------------------------------------------------------------------
## SYNTAX ##
#         for variable in sequence:
    # block of code to be executed
#-------------------------------------------------------------------------

## EXAMPLES ##
# Taking input from the user 
n= int(input("Enter the number:"))

## Problem 1: Print 1 to n
for i in range(1,n+1):
    print(i)

print("------------------------------")

## Problem 2: Reverse For loop. Print n to 1
for i in range(n,0,-1):
    #since coming backward it's imp to give step
    # coming one step back therefore, -1
    print(i)