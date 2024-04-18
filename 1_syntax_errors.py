#In python there are two types of issues that can break your code
#--stop the exectuion of your code and throw and error

#Syntax Error : errors in your codes "grammar" a structural error
#--- misspelling
#--- indentation errors
#--- code structures missing or overly presents
#---- colons, indentation, parenthesis, ' ', " " 

#example 1

x = 1

if x > 0:
    print('postive number')


#example 2

x = 1

if x > 0:
    print("postive number")

#example 2


x = -1

if x > 0:
    print("postive number")
print('out of the code block')