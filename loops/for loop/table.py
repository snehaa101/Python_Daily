#----------------------------------------------------
# Topic: PYTHON LOOPS
# Problem: Take a number as input and pritn a table
# ---------------------------------------------------

#taking the input from the user
n = int(input("Enter the you want a table of: "))

#loop for just printing the ans
for i in range(1,11):
    num=n*i
    print(f"{num}")

#loop for table in {2*1=2} form
print("table in {2*1=2} form")
for i in range(1,11):
    print(f"{n}*{i}={n*i}")    