#-------------------------------------------------------
# Topic : Python Loops (FOR LOOP)
# Description :
#          - Syntax
#          - Simple examples of using basic FOR loop 
#-------------------------------------------------------
## With the while loop we can execute a set of statements as long as a condition is true.

##Check condition
# ↓
# If True → Run loop body
# ↓
#increment to avoid infinite loop
# ↓
# Go back and check condition again
# ↓
# Repeat until condition becomes False

## SYNTAX
        #   while(condition){
        #     -------body-----
        #   }
#------------------------------------------------------

## EXAMPLE ##

#-print hey 100 times

counter= 0 # starting value

#loop runs 100 times
while counter<100:
        print("heyy....!!!!")
        #increment to avoid infinite loop
        counter += 1 
#-------------------------------------------------

#-print 1 to 10

i=1 #initialzing

#loop prints till 10
while i<=10:
        print(i)
        #increment to avoid infinite loop
        i+=1
