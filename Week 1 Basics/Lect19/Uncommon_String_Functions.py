print("\nCapitalize():")
c="kolkata"
print(c.capitalize()) #capitalize the first letter of first word temporarily
print(c)    #there is no cahnge in c

print("\ntitle():")
d = "it is raining today"
print(d.title()) #capitalize every word's first letter
print(d)         # does not cahnge the original d


print("\nupper(): lower():")
e="Sushant Kumar"
print(e.upper()) # capitalize every letter of every word
print(e.lower()) # lower case every letter of every word
print(e)         # No change in original varible 

print("\nswapcase():")
f="Sushant Kumar"
print(f.swapcase())
print(f)

print("\ncount():")
g="sushiii"
h="it is raining in sing"
print(g.count("i"))
print(h.count("ing"))

print("\nfind() index()")
j="sushant"
print(j.find("u")) #gives the index of the character passed(this doesnot throw error when not found, returns -1)
print(j.index("a")) #this also returns the index of character passed but the difference is index returns error if not found


print("\nendswith() startswith()")
j="it is raining outside"
print(j.endswith("ide"))
print(j.endswith("fge"))

print(j.startswith("it "))
print(j.startswith("gfe "))

print("\nformat():")
k="my name is {}, and my age is {}"
print(k.format("Sushant",20))


l="Hello my name is {1}, and i am {0}" #1 and 0 decides the position inside the format parameters passing

print(l.format("Sushant",30))

m="Hello my name is {name}, and i am {age}" #age and name decides which bracket will take what parameter
n="Hello my name is {age}, and i am {name}" #age and name decides which bracket will take what parameter

print(m.format(name="Sushant",age=30))
print(n.format(name="Sushant",age=30))


print("\nisalnum(),isalpha(),isdecimal(),isdigit(),isidentifier()",sep="/")

print("Hello".isalpha())    # True (only letters)
print("Hello123".isalpha()) # False (contains numbers)
print("Hello!".isalpha())   # False (contains special character)
print("".isalpha())         # False (empty string)

print("Hello123".isalnum())  # True (only letters and numbers)
print("Hello".isalnum())     # True (only letters)
print("123".isalnum())       # True (only numbers)
print("Hello 123".isalnum()) # False (contains space)
print("Hello!".isalnum())    # False (contains special character)

print("123".isdigit())    # True (only digits)
print("12.3".isdigit())   # False (contains a dot)
print("123a".isdigit())   # False (contains a letter)
print("".isdigit())       # False (empty string)

print("hello".isidentifier())   # True (valid variable name)
print("_var".isidentifier())    # True (valid variable name)
print("123name".isidentifier()) # False (cannot start with a number)
print("name with space".isidentifier()) # False (contains space)
print("for".isidentifier())     # True (but it's a Python keyword)



print("\n Split()")
x="Who is the pm of india"
print(x.split())    #we can alse use this inside list

# using for loop to access the list listt
listt=x.split()
for i in listt:
    print(i)


print("Hello123".isalpha()) # False (contains numbers)





