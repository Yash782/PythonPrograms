# Taking number input from user into list and counting number odd and even numbers in it.
# Creating a variable for list
lst = []
# Variable for storing number of elements
n = int(input("Enter the number of elements: "))

# This for loop will take 'n' number of inputs and append to list.
for u in range(0, n):
    element = int(input(f'Enter the number {u + 1}: '))
    lst.append(element)

# Printing the list:)
print(f'You list is: {lst}')


""" This functions counts the number of odd and even number with using if else statement
and counter for even and odd number """
def odd_even(lst):
    e = 0
    o = 0
    for i in lst:
        if i % 2 == 0:
            e += 1

        else:
            o += 1
    return e, o

# Calling the function
even, odd = odd_even(lst)

# Printing the values
print(f'Even={even} and Odd={odd}')
