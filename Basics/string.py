# a= "sneha" [double quoted string]
# b= 'sneha' [single quoted string]
# c= '''sneha'''[triple quoted string][also multiline string]

name="sneha"

#indexing= variable_name[index_start : index_end] {ending index is always excluded}

index1= name[0:3]#start from index 0 till 3(excluding3)
print(index1)

index2= name[1:4]
print(index2)

#index=name[ : index_end] ; blank=0 
#index=name[index_start : ] ; blank= n^th index

# NEGATIVE INDEXING - index= name[-4:-1]
# direct convert indexes -ve to +ve & swap, that's ans

# SLICING  

print(len(name)) #tells length of string
print(name.capitalize()) #makes 1st letter of string capital
print(name.replace("sneha","hope"))

name= input("enter a name :")
name= name.strip() #remove the white space from input string
name= name.capitalize()#make the 1st letter captital in case of all small
print(f"hey!, {name}")
# INPUT: enter a name :         naman    
#OUPUT: hey!   klaus   

