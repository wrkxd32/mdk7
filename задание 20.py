#1
x = 10

def local_scope():
    x = 5
    print(x)
    print(globals()['x'])

local_scope()

#2
def outer():
    y = 20
    def inner():
        nonlocal y
        y = 30
        print(y)
    inner()
    print(y)

outer()

#3
z = 1

def modify():
    z = 2
    print(z)
    print(globals()['z'])

modify()

#4
def check_built_in(my_list):
    length = len(my_list)
    print("длина: :", length)

check_built_in([1, 2, 3, 4, 5])

total = 0

#5
def cv(numbers):
    global total
    total = 100 - sum(numbers)
    return total

result = cv([10, 20, 30])
print(result)
print(total)