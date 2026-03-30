# aermstrong num -  positive n digit number that equals the sum of its digits each raised to the power of n
# EXAMPLE - 153 = 1^3 +5^3+ 3^3 =153

n = int(input("enter an number : "))
num = n  # for saving original input before applying loop on it
total = 0
power = len(str())  # counts the length of n

while n > 0:
    digit = n % 10  # extract last digit
    total += digit**power  # adding digit^power to total
    n = n // 10  # removes the last digit

# using condition to compare with the original
if total == num:
    print("the number is armstrong")
else:
    print("the number is not armstrong")


""" DRY RUN

enter an number : 153

num = 153,  power = 3,  total = 0

Loop 1:  digit = 3,  total = 0 + 27   = 27,   n = 15
Loop 2:  digit = 5,  total = 27 + 125 = 152,  n = 1
Loop 3:  digit = 1,  total = 152 + 1  = 153,  n = 0

Loop ends → total(153) == num(153) → the number is armstrong"""
