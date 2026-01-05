#-------------------------------------------------------
# Topic : Python Conditions (if statements)
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

#-----------------------------------------------------

## LARGEST NUMBER
b=int(input("Enter first number :"))
c=int(input("Enter second number :"))

if (b>c):
    print(b," is greater")
else:
    print(c," is greater")

#----------------------------------------------------

## PRINT LAST DIGIT and IF DIV BY 5
num = int(input("Enter the number : "))

last_digit= num % 10
print(f"The last digit of the {num} is {last_digit}")

if last_digit % 5==0 :
    print(f"{last_digit} is divisible by 5")
else:
    print(f"{last_digit} is NOT divisible by 5")

