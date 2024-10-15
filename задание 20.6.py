# 1
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(5))

# 2
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))

# 3
doub = lambda x, y: x * y
print(doub(5, 8))

# 4
sl = ["Приветствую", "Привет", "Как дела?"]
vv = list(map(lambda s: s.upper(), sl))
print(vv)

# 5
flt = list(filter(lambda s: len(s) > 3, sl))
print(flt)

# 6
l1 = [477, 490, 888]
l2 = ['a', 'b', 'c']
pp = list(zip(l1, l2))
print(pp)

# 7
def pairwise_sum(l3, l4):
    return [a + b for a, b in zip(l3, l4)]

print(pairwise_sum([1, 2, 3], [4, 5, 6]))

# 8
def unzip_lists(pairs):
    return list(zip(*pairs))

aa = [(1, 'a'), (2, 'b'), (3, 'c')]
u = unzip_lists(aa)
print(u)