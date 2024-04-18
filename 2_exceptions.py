#Exceptions are the other big issue that can cause your program to break/ stop executing

#Exceptions : arise when out code is set up correctly, but some operations don't execute for 
# a variety of reasons.

#--- ZeroDivisionError : occurs when you try to divide by 0

quotient = 10/0


#--- NameError : try to call a var or a func before it was defined.

print(x)
print(doubler())


#--- ValueErrors : performing operations with invalid values

str_num = 'nine'
int_num = int(str_num) #trying to convert and invalid value

my_list = ['apple', 'banana', 'orange']
my_list.remove('grapes') #because grapes are not in the list, they are an invalid value

#--- TypeError : trying to perform operations on values of inappropriate type.

num = 5
total_people = num + ' people' #cannot add/concatenat a str and int together

#--- AttributeError : trying to use methods on improper objects (the wrong datatype)

word = 'Hello'
rword = word.reversed()

word.append(' World')

