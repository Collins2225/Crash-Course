"""
Booleans in Python — A Clear, Complete Introduction
A boolean is a data type with only two possible values:

True

False

They are used for:

decisions

conditions

comparisons

loops

logic

Booleans are the backbone of how programs “think.”


1. Booleans for Decisions
A program often needs to choose between two paths.

Example:
is_raining = True

if is_raining:
    print("Take an umbrella")

    Here, the boolean True decides which code runs.
    if the boolean is flase it doesn,t print anything     

Why it matters
Booleans let your program behave differently depending on the situation.

2. Booleans for Conditions
Conditions are expressions that evaluate to True or False.

Example:

age = 20

if age >= 18:
    print("You can vote")
in this case age is greater than 18 so you can vote
if age is not greater than 18 you can,t vote     

3. Booleans for Comparisons
Every comparison in Python returns a boolean.

Example:
print(5 > 3)     # True
print(10 == 5)   # False

Comparisons are the foundation of logic.

Why it matters
Comparisons let your program understand relationships between values.

4. Booleans for Loops
Loops often run while a condition is True.

Example:
count = 3

while count > 0:
    print(count)
    count -= 1

5. Booleans for Logic

When we talk about logic in programming, we mean the ability to combine or modify boolean values to create more complex decisions.

Python gives you three logical operators:

and

or

not

These operators let your program “think” by combining True/False values.

1.and — Both Must Be True
and returns True only if both sides are True.

Examples

True and True      # True
True and False     # False
False and False    # False

age = 20
has_id = True

age >= 18 and has_id   # True

This means:
“You can enter only if you are 18+ and you have ID.”

2. or — At Least One Must Be True
or returns True if at least one side is True.

Examples
True or False      # True
False or True      # True
False or False     # False

is_weekend = True
is_holiday = False

is_weekend or is_holiday   # True

3. not — Flips the Value
not turns True → False and False → True.

Examples
not True     # False
not False    # True

is_logged_in = False

not is_logged_in   # True

Why This Matters
Logic operators let you build complex conditions:

age = 25
has_ticket = True
is_vip = False

(age >= 18 and has_ticket) or is_vip


"""

# is_raining = False

# if is_raining:
#     print("Take an umbrella")

# age = 11

# if age >= 18:
#     print("You can vote")

# count = 7

# while count > 0:
#     print(count)
#     count -= 1

# is_schooltime = True

# if is_schooltime:
#     print("microcontroller")

# name= "collins"

# if name is "collins":
#     print(name)

print(False or 0)
print(5 + True == 6)
print(bool("0"))
print(bool(""))
print(3!=3)

print(10=="10")

print(5 > 2)
