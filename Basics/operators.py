# ARTHMETIC OPERATIONS
a=5
b=2
sum=a+b
print(sum)
#OR
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #MODULO: gives remainder
print(a**b) #a^b

# COMPARISION OPERATORS [output always bool]
x=50
y=20

print(a==b)
print(a!=b)
print(a>b)
print(a<b)  

# ASSIGNMENT OPERATORS
num=3
# num= num + 2 OR
#num+=2 #5
#num-=2 #1
#num*=2 #6
#num/=2 #1.5
#num%=2 #1
#num**=2 #9
print(num)

#LOGICAL operator
val1= True
val2= False

print("and operator",val1 and val2)
print("or operator",val1 or val2)
print("not operator",not val1)
print("not operator",not val2)


#--when a variable have same value in order to save
#--memory python refer to same loc whenever any of them
#--is called,
#  also if var2 value is updated it won't affect var1
var=10
print(var,id(var))
var2=10
print(var2,id(var2))
var2=20
print(var2,id(var2))
