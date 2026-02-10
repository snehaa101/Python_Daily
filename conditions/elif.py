#-------------------------------------------------------
# Topic : Python Conditions (if statements)
# Description :
#          Simple examples of using basic if statements
#-------------------------------------------------------

### SYNTAX ###

    # if (condition):
    #    ---body---
    # elif (condition): # can put infinite elifs
    #    ---body---
    # else:
    #    ---body---  # else - not compulsory

#***EXAMPLES***

#### P1 #### 
# Asking 5 subject marks from user and calculate percentage and print it.
    #  81-100 -> A
    #  61-80 -> B 
    #  51-60 -> C 
    #  31-50 -> D
    #  1-30 -> FAIL 
    #  INVALID

# Prompt input from user
maths=int(input("enter marks of maths = "))
english=int(input("enter marks of english = "))
science=int(input("enter marks of science = "))
history=int (input("enter marks of history = "))
hindi=int(input("enter marks of hindi = "))

#calculating total marks
Total = maths + science + english + hindi + history
#calculating percentage
percentage = float(Total/500)*100
print(f"percentage scored = {percentage}%")

# using else-if for telling the grade
if percentage>=81 and percentage<=100:
    print ("Congrats..!! you got an A ")

elif percentage>=61 :
    print("Well Done! you got B grade")

elif percentage>=51 :
    print("DO better!! you got C grade")

elif percentage>=31 :
    print("Hardwork needed you got D")

elif percentage>=1 :
    print("Sorry you FAILED")
else:
    print("INVALID") # percentage > 100



#### P2 #### 
# GREATER NUMBER 

a = int(input("enter the first number : "))
b = int(input("enter the second number : "))

if a>b:
    print(f"{a} is greter than {b}")
elif b>a:
    print(f"{b} is greter than {a}")
else:
    print(f"both numbers are equal")