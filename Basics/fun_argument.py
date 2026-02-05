# info can be passed into fun. as arguments
# syntax = fun_name(argument1,argument2,.....etc)

# ** default arguments**
def average(a=9, b=1):
    print("The average is ", (a+b)/2)
average(4,5)#giving values of both a and b
average(b=9)#giving only one value and [a = default value i.e given in fun]
average()

# **keyword arguments**