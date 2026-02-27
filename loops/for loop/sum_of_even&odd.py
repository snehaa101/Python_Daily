#-------------------------------------------------------------------------
# Topic: PYTHON LOOPS (for loop)
# Problem: Print the sum of all even and odd number in a range separately
#-------------------------------------------------------------------------

n=int(input("Enter a number:"))

even=0
odd=0

for i in range(1,n+1):
    if i%2==0:
        even +=i
    else:
        odd+=i
print(f"The sum of all odd numbers among {n} numbers is {odd}.\nand\nThe sum of all even numbers among {n} numbers is {even}")