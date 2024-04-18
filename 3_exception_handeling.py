
#Handeling Exceptions with Try and Except

#--- try : allows us to try a codeblock that will potentially raise an exception

#--- except : in the event that you run into an exception, we execute the except block instead
#without terminating our program with an Error message

try:
    x=1
    print(x+'person')
except:             #generic except handler
    print('Sorry cant do that') 


#Specifc Exceptions : to respond with a particular message for a specific kind of Error



# try:
#     div = int(input('Give me a number to divided 10 by: '))
#     quotient = 10/ div
#     print(f'10 divided by {div} = {quotient}')
# except ValueError:
#     print('Make sure to respond only with numbers!')
# except ZeroDivisionError:
#     print('You cant divide by 0')
# except:
#     print('Invalid Input')


#--- else : an additional code block that executes only when the try block succeeds


while True:
    try: 
        age = int(input('How old are you? '))
        birthday = age + 1
    except ValueError:
        print('Please respond only with numbers!')
    except:
        print('Invalid Response')
    else:
        print(f'On your birthday you will be {birthday} years old')
        break


#--- finally : an additional code block that executes regardless of whether your try block succeeds or not

groceries = ['apple', 'walnuts', 'pear','bread']

while True:
    try:
        item = input('What item do you want to remove? ')
        groceries.remove(item)
    except ValueError:
        print(f'You dont have {item} on your list')
    except:
        print('Invalid Input')
    else:
        print(f'Successfully removed {item}')
        break
    finally:       #This block executes regardless of whether try succeeded or not
        print('Your current list:')
        print('~~~~~~~~~~~~~~~~~~~')
        for item in groceries:
            print(item)


#--- raise : raise our own custom Exception 

while True:
    print(''' 
    Choose an Action
    -----------------
    1.) Account Info
    2.) Settings
    3.) Log Out
''')
    try:
        action = input('Action: ')
        if not action in ['1', '2','3']:
            raise ValueError
    except ValueError:
        print('Invalid Selection, please choose 1, 2, or 3')
    except:
        print('Invalid Input')
    else:
        if action == '1':
            print('Accessing Account Info')
        elif action == '2':
            print('Opening Settings')
        elif action == '3':
            print('Logging Out -- Goodbye!')
            break
