#---------------------------------------------------------------------------------------
# Topic: Condition Statments
# Problem: Triangle's Inequality Theorem
#              - It states that the sum of the lengths of any two sides of a triangle 
#                must be greater than the length of the third side,
#                then the triangle can be formed.
# --------------------------------------------------------------------------------------

# Taking the input from user
S1= int(input("Enter the first side of triangle: "))
S2= int(input("Enter the second side of triangle: "))
S3= int(input("Enter the third side of triangle: "))

if S1+S2>S3 and S1+S3>S2 and S2+S3>S1:
    print("The triangle is possible")
else:
    print("The triangle is not possible")