import random

#1
print(random.randint(1, 100))

#2
fr = ['Яблоко', 'Банан', 'Груша']
print(random.choice(fr))

#3
numbers = list(range(1, 11))
random.shuffle(numbers)
print(numbers)

#4
rnd_nmb = [random.randint(1, 50) for _ in range(5)]
print(rnd_nmb)

#5
clr = ['Красный', 'Черный', 'Желтый']
rr = [random.choice(clr) for _ in range(4)]
print(rr)

#6
def gr():
    ysl = int(input("Количество граней куба: "))
    nn = []
    while True:
        nn.append(random.randint(1, ysl))
        if input("Бросить еще раз? ").lower() != 'да':
            break
    print(f"Количество бросков: {len(nn)}\nРезультат: {nn}")
gr()

#7
def passwd(length):
    ch = ''.join(chr(i) for i in range(32, 127))
    asd = ''.join(random.choice(ch) for _ in range(length))
    print(asd)
passwd(12)