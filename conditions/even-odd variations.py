#----------------------------------------------------
# Topic: Condition Statments
# Problem: Even Odd Variations
# ---------------------------------------------------

## The Common Input for below questions
a = int(input("enter the number : "))

# Variation-1 (Basic Even and Odd)
if a%2==0 :
    print (f"{a} is an even number")
else:
    print (f"{a} is an odd number")


# Variation-1 POSITIVE/NEGATIVE + EVEN/ODD
if a==0:
    print("0 is an even number but neither positive or negative")

elif a>0:
    if a%2==0 :
        print (f"{a} is an positive even number")
    else:
        print (f"{a} is an positive odd number")

else:
    if a%2==0 :
        print (f"{a} is an negative even number")
    else:
        print (f"{a} is an negative odd number")
