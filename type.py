x = 5
y = "john"
print(type(x))
print(type(y))


# multiple values
x, y, z = "cherry", "apple", "orange"
#print(x)
#print(y)
#print(z)



# unpack collection
fruits = ["apple", "cherry", "banana"]
x, y, z = fruits
print(x)
print(y)
print(z)





# global variables
x = "divine"

def myfunc():
   print("i am "+ x)
myfunc()

    