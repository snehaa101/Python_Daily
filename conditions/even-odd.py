## The Common Input for below questions
a = int(input("enter the number : "))

# (1) # Accept an integer and check whether it is an EVEN or an ODD number

if a%2==0 :
    print (f"{a} is an even number")
else:
    print (f"{a} is an odd number")

# (2) # Accept an integer and check whether it is an POSITIVE EVEN or ODD number OR an NEGATIVE EVEN ODD

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
