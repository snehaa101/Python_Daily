#-------------------------------------------------------------------------
# Topic: PYTHON LOOPS (for loop)
# Problem: WAP a program to reverse string without function
#-------------------------------------------------------------------------

#reverse string is a string which is same as original string but in reverse order.

# Taking input from user
s = input("Enter a string: ")

#range(start,stop,step)

#START is the starting index of the string which is 0 by default
        # in this case it'll be length of a string - 1 [i.e len(a)-1] since starts with 0 
        # eg: git [g-0; i-1; t-2 ] here length is 3 but starts with 2
#STOP is the index where the loop will stop but it will not include that index
        # in this case snce we have to go till 0 we'll write -1
#STEP is the value by which the index will be incremented or decremented
        # here it's decrement hence, 1
        
for i in range(len(s)-1,-1,-1):
        print(s[i],end="")