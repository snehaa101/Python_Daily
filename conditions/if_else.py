#-------------------------------------------------------
# Topic : Python Consitions (if statements)
# Description :
#          Simple examples of using basic if statements
#-------------------------------------------------------

### SYNTAX ###

#   if(condition):
#     ---body--
#   else:
#     --body---

# ***EXAMPLES***

## VOTING AGE
a=int(input("Enter your age : "))
print ("Your age is ",a)

   # conditional operator [==,<,>,<=,>=.!=]
if (a>=18):
    print(" You can drive")
else:
    print("You cannot drive")

#--------------------------------------------
## LARGEST NUMBER
b=int(input("Enter first number :"))
c=int(input("Enter second number :"))

if (b>c):
    print(b," is greater")
else:
    print(c," is greater")

#---------------------------------------------
## EVEN ODD
if (b % 2 == 0):
    print(b," is even.")
else:
    print(b," is odd.")