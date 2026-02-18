#Python uses a built‑in function called len() to count how many characters are in a string.

len("Hello") #5

len("Python")        # 6
len("12345")         # 5
len("Hi!")           # 3
len("Hello world")   # 11  (space counts)
len(" ")             # 1   (a single space)

len("a b c")   # 5
len("")   # 0

len(123)      # error
len(str(123)) # 3

print(len("\n"))        # 1
print(len("\t"))        # 1
print(len("Python"))    # 6
print(len("Hello world"))  # 11
print(len("12345"))     # 5
print(len("Hi!"))       # 3
print(len("   "))       # 3
print(len(""))          # 0
print(len("True"))      # 4
print(len("False "))    # 6
print(len("A\nB"))      # 3
print(len(str(2026)))   # 4