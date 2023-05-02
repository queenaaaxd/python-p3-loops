#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while (i > 0):
        print(i)
        i-=1
    print("Happy New Year!")



# list comprehension
def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]

print(square_integers([1, 2, 3, 4, 5]))

        

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if (not i % 15):
            print("FizzBuzz")
        elif (not i % 5):
            print("Buzz")
        elif (not i % 3):
            print("Fizz")
        else:
            print(i)

    