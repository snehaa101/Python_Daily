#-------------------------------------------------------
# Topic : Python Conditions (nested if else statments)
# Description :
#          Simple examples of using nested if else statements
#-------------------------------------------------------

### SYNTAX ###

#   if(condition):
#       if(condition):
#              ---body--
#       else:
#            --body---
#   else:
#       --body---
#---------------------------------------------------------
# ***EXAMPLES***

## POSITIVE OR NEGATIVE NUMBER

number = int(input("Enter a number: "))

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
        print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')


## SAMPLE OUTPUT 1
#Enter a number : 1
#Number is positive

## SAMPLE OUTPUT 2
#Enter a number : 0
#Number is 0

## SAMPLE OUTPUT -1
#Enter a number : 0
#Number is negative