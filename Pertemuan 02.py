#Phyton Functions
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

add_numbers(2, 4)

def find_square(num):
    result = num * num
    return result

square = find_square(2)

print('Square:', square)

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Gilang', first_name = 'Tangguh')

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

find_sum(1, 2, 3)

find_sum(4, 9)

message = 'Hello'

def greet():
    print('World', message)

greet()
print('Gilang', message)

# outside function 
def outer():
    message = 'local'

    def inner():

        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

c = 1

def add():
    print(c)

add()

c = 1 

def add():

    global c

    c = c + 2 

    print(c)

add()

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

import math

print("The value of pi is", math.pi)

def main():
    print("Hello World")

if __name__=="__main__":
    main()

import os

print(os.getcwd())