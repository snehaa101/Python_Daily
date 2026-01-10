# "def" - define function KEYWORD
#NORMAL CODE [to fine gmean]
 #for a,b
a=9
b=81
# gmean1 = (a*b)/(a+b)
# print(gmean1)
##[to find greater no.]
# if(a>b):
#      print("first number is greater = ",a)
# else:
#      print("second number is greater = ",b)

#  #for c,d
c=5
d=4
# gmean2 = (c*d)/(c+d)
# print(gmean2)
##[to find greater no.]
# if(c>d):
#      print("first number is greater = ",c)
# else:
#      print("second number is greater = ",d)

#creating a function to calculate GMEAN
def calculatinggmean(a,b):
     gmean = (a*b)/(a+b)
     print(gmean)

#function for greater number
def greaterno(c,d):
     if(c>d):
       print("first number is greater = ",c)
     else:
      print("second number is greater = ",d) 


calculatinggmean(a,b)#recalling function for gmean
greaterno(a,b)#recalling function for greater no


calculatinggmean(c,d)
greaterno(c,d)