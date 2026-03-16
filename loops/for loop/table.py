# ----------------------------------------------------
# Topic: PYTHON LOOPS
# Problem: Take a number as input and pritn a table
# ---------------------------------------------------

# taking the input from the user
n = int(input("Enter the you want a table of: "))

# loop for just printing the ans
for i in range(1, 11):
    num = n * i
    print(f"{num}")

# loop for table in {2*1=2} form
print("table in {2*1=2} form")
for i in range(1, 11):
    print(f"{n}*{i}={n*i}")


"""
SAMPLE OUTPUT : 

Enter the you want a table of: 5
5
10
15
20
25
30
35
40
45
50
table in {2*1=2} form
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50

"""
