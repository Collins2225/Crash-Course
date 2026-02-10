"""
 Python Data Types — A Clean, Clear Introduction
 Python has several built‑in data types, but the core ones you’ll use constantly are:

 1. Integers (int)
 Whole numbers, positive or negative.

 Examples:

 5

0

-12

Used for counting, indexing, loops, math.
"""

"""
Floats (float)
Numbers with decimals.

Examples:

3.14

0.0

-2.5

Used for precise calculations, division, measurements.

"""

"""
Strings (str)
Text inside quotes.

Examples:

"Hello"

'Python'

"123" ← still a string, not a number

Used for messages, labels, file names, user input.

"""

"""
Booleans (bool)
Only two values:

True

False

Used for conditions, logic, comparisons.
"""

"""
None (NoneType)
Represents “no value” or “empty”.

Example:

None

Used when a function returns nothing or a variable is intentionally empty.
"""

"""
Why Data Types Matter
Every operation in Python depends on the type:

"5" + "5" → "55" (string glue)

5 + 5 → 10 (math)

"5" * 3 → "555" (string repeat)

5 * 3 → 15 (math)

int("5") → 5 (conversion)

Understanding types is the foundation of writing correct, predictable code.
"""
type(5) # integer

type(3.14) # float

type("Hello") # strings

type(True) # boolean

type("123") #string

type(float(10)) #float

type("True") #string

type(None) #none

type(5 > 3) #boolean 5 > 3 it evaluates true

print(type(10 + 5.0)) # <class 'float'>

print(type("5" * 2)) #55
 
print(int(3.9)) # 3

print(float("10") + 5) #15.0

print("Age: " + str(20)) # Age 20

print(bool("")) #False

print(bool("False")) #True

print(type(None))#<class 'NoneType'>

print(str(3) * 3) #333

print(int("5") + float("2.5")) #7.5



