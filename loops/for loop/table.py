#----------------------------------------------------
# Topic: PYTHON LOOPS
# Problem: Take a number as input and pritn a table
# ---------------------------------------------------

#taking the input from the user
n = int(input("Enter the you want a table of: "))

for i in range(1,11):
    num=n*i
    print(f"{n}*{i}={num}")

    