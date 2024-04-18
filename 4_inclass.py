#Inclass 1

# **Problem Statement**:
# An online bookstore is processing orders for a popular novel. They need a simple system to ensure that customers enter a valid quantity when placing their orders.

# **Instructions**:



# 4. If the input is invalid (not an integer or a negative number), display an error message and prompt the user again.



# using input() ask user how many books

# check type() of input or isinstance(), rely on try except to handel invalid input

# else block to show a order confirmation message, if try block succeeds

# except : to handel invalid data and respond with error message
#--- ValueError : if they give me a 'nine' insted of 9
#--- raise ValueError : specific value error to tell about negative numbers

# While loop to continuosly ask, and only break once they successfully make it through try



while True:
    try:
        num_books = int(input('How many books do you wish to order: '))
        if num_books <= 0:
            raise ValueError('no negative values')
    except ValueError as ve:
        if 'no negative values' in str(ve):
            print('You cant order a negative amount of books')
        else:
            print('Please respond with numbers only.')
    else:
        if num_books == 1:
            print('Thank you for ordering a book')
        else:
            print(f'Confirming order of {num_books} books.')
        break