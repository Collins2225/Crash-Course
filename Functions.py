"""
Functions are one of the biggest turning points in Python because they let you organize your code, 
avoid repetition, and build programs that scale. 
Everything you’ve learned so far—variables, operators, tuples—comes together inside functions.

A function is a reusable block of code that performs a specific task. You define it once, and you can call it as many times as you want.

A function is like a little machine you build.

You give it something…

It does something…

And it gives you something back.

Just like a toy vending machine:

You put in a coin

The machine works

You get a toy

""" 
def machine():
    print("Toy!")
machine()

""" Why we use functions
Because they help you not repeat yourself.

Imagine you want to draw a age 10 times.
Instead of drawing it again and again, you make a sun‑drawing machine. """


def age():
    print("30")
age()
age()
age()
age()
age()

""" 
Functions with names
Just like your toys have names, functions have names too. 
"""
def greet():
    print("Hello!")
greet()

""" functions that take inputs
Imagine a lunchbox.
You put an Carrot inside, and the lunchbox gives you a sliced Carrot. """

def vegetables(vegetables):
    print("Here is your sliced", vegetables)
vegetables("Carrot")
vegetables("Cabbage")

""" Functions that give something back
Some machines give you something out.
 """
def multiplication(x, y):
    return(x * y)
result = multiplication(7, 5)
print(result)

def substraction(z , x):
    return(z - x)
outcome= substraction(9, 4)
print(outcome)

""" 
Functions can return many things
Like a surprise box with many toys inside. """


def food():
    return "rice", "chicken", "fish"
m, n ,o=food()

print(m)

""" Functions inside functions
Imagine a house with a small room inside.

 """
def big_house():
    def small_room():
        print("I am inside!")
    small_room()
big_house()

def university():
    def lecture_room():
        print("i am learning in the Lecture room")
    lecture_room()
university()       

""" Tiny functions (lambda)
These are like one‑line magic tricks. """

square = lambda a: a * a
print(square(5)) #25

square = lambda x: x*x
print(square (6)) #36




