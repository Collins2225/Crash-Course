"""
Python Operators — A Clear, Complete Guide
Operators are symbols that tell Python to perform an action.
You’ve already used many of them without realizing it.

Python has five major categories of operators:

1.Arithmetic operators

2.Comparison operators

3.Logical operators

4.Assignment operators

5.Membership operators

6.Identity operators

1. Arithmetic Operators
5 + 3      # Addition: result is 8
10 - 4     # Subtraction: result is 6
6 * 7      # Multiplication: result is 42
10 / 4     # Division: result is 2.5 (always float)
10 // 4    # Floor division: result is 2 (cuts off decimals)
10 % 4     # Modulus: remainder of 10 ÷ 4, result is 2
2 ** 3     # Exponent: 2 raised to the power of 3, result is 8

2. Comparison Operators
5 == 5     # Equal: True
5 != 3     # Not equal: True
7 > 2      # Greater than: True
2 < 1      # Less than: False
5 >= 5     # Greater or equal: True
3 <= 4     # Less or equal: True

3. Logical Operators
True and False     # and: both must be True → result is False
True or False      # or: at least one True → result is True
not True           # not: flips the value → result is False

4. Assignment Operators
x = 5       # Assign: store 5 in x
x += 3      # Add and assign: x = x + 3 → x becomes 8
x -= 2      # Subtract and assign: x = x - 2
x *= 4      # Multiply and assign: x = x * 4
x /= 2      # Divide and assign: x = x / 2
x **= 3     # Exponent and assign: x = x ** 3

5. Membership Operators
"a" in "cat"        # True: "a" is inside "cat"
"z" not in "cat"    # True: "z" is not inside "cat"

6. Identity Operators
x = None
x is None           # True: x is the same object as None
x is not None       # False: x is not a different object



"""
x = 10//3
print(x)

x=7%3
print(x)

x="py" in "python"
print(x)

x = 5
x += 2
print(x)

print(not (5 > 2))

print(3 * 2 ** 2)

print("z" not in "pizza")

x = None
x is None
print(x)

print(10 - 3) * 2


