"""
A tuple is an ordered collection of items, just like a list, but with one major difference:

Tuples cannot be changed.
This property is called immutability. 

You create a tuple using parentheses:
my_tuple = (1, 2, 3)

Tuples Are Ordered
The items keep their position.

t= ("0.3",2,5,5)
print(t[0])
print(t[1])
print(t[2])
print(t[3])

Tuples Are Immutable
You cannot change, add, or remove items.
t = (1, 2, 3)
t[0] = 10     #  Error: tuples cannot be modified

Tuples Allow Duplicate Values
t = (1, 1, 2, 3)

Tuples Support Indexing and Slicing
Just like strings and lists:
t = (10, 20, 30, 40, 50)

print(t[1])      # 20
print(t[1:4])    # (20, 30, 40)

Indexing Examples
t = (10, 20, 30, 40)

print(t[0])   # 10  → first item
print(t[1])   # 20  → second item
print(t[3])   # 40  → fourth item
print(t[-1])  # 40  → last item (negative index)
print(t[-2])  # 30  → second from the end

Slicing Examples
Slicing means taking a range of items.
t = (10, 20, 30, 40, 50)

print(t[1:4])    # (20, 30, 40) → from index 1 up to (not including) 4
print(t[:3])     # (10, 20, 30) → from start to index 3
print(t[2:])     # (30, 40, 50) → from index 2 to end
print(t[:])      # (10, 20, 30, 40, 50) → whole tuple
print(t[::2])    # (10, 30, 50) → step of 2


Tuple With One Item Needs a Comma
x = (5)      #  Not a tuple, just an integer
y = (5,)     #  This is a tuple

x = (5,)
print(type(x))   # <class 'tuple'>

# unpack Tuples
food=("garri", "manka")
g,m=food

print(m)

movies=("money heist", "prison break")

p,m=movies
print(p)

person = ("Collins", 21, "Latvia")
name, age, country = person
print(name)
print(age)
print(country)


numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5


data = (10, 3.14, True, "robotics")
a, b, c, d = data

numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

Nested Tuples — Tuples Inside Tuples


"""
# t= ("0.3",2,5,5)
# print(t[0])
# print(t[1])
# print(t[2])
# print(t[3])


# A=(3, 4, 5, 6)

# print(A[1:3])

# t=(12,14,16,18,20)

# print(t[1:4])
# print(t[::3])
# print(t[2:])
# print(t[:])

# t=(5,)
# print(t[0])



# t = (1, 2, 3)
# print(len(t))

# t = (5, 6, 7, 8)
# print(t[1:3])

# t = (10, 20, 30)
# print(t[1])

# t = (4,)
# print(type(t))

# a, b = (9, 10)
# print(a + b)

# person = ("Collins", 21, "Latvia")
# name, age, country = person
# print(name)
# print(age)
# print(country)


# data = (10, 3.14, True, "robotics")
# a, b, c, d = data


Anime=((0,2), (2,4), (3,5))

print(Anime[0][1])



