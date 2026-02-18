#----------------------------------------------------
# Topic: Condition Statments
# Problem: Divisible by 2 and 3
# ---------------------------------------------------

num= int(input("Enter the number you would like to check divisibility : "))

if num%2==0 and num%3==0:
    print(f"{num} is divisible by 2 and 3 ")

elif num%2!=0 and num%3==0:
    print(f"{num} is only divisible by 3 and not 2")

elif num%2==0 and num%3!=0:
    print(f"{num} is only divisible by 2 and not 3")

else:
    print(f"{num} is not divisible by 2 and 3 ")