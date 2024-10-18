#1 (Арифметическая сумма)
'''def fn(defoln=0.000001):
    rstt = 0.0
    n = 1
    while True:
        m = 1 / n
        if m < defoln:
            break
        rstt += m
        n += 1
    return round(rstt, 9)

kolvo1 = input("Значение E: ")
defoln = float(kolvo1) if kolvo1 else 0.000001

res3 = fn(defoln)
print(res3)

#2
def fnct3(defoln=0.000001):
    c = 0.0
    n = 1
    while True:
        d = n / (n ** 2)
        c += d
        if d < defoln:
            break
        n += 1
    return round(c, 9)

try:
    rr3 = input("Значение E: ")
    if rr3.strip():
        original = float(rr3)
    else:
        original = 0.000001
        
    res4 = fnct3(original)
        
    print(res4)

except ValueError:
    print("Ошибка")'''

#3
import math as m
'''
def fnctn11(defoln=None):
    df = 0.0
    n = 2
    while True:
        l = m.log(n) / n
        df += l
        if defoln is not None and l < defoln:
            break
        n += 1
    return round(df, 9)

zn1 = input("Значение E: ")
defoln = float(zn1) if zn1 else 0.000001
ress1 = fnctn11(defoln)
print(f"Итог: {ress1}")

#4
def fnc2(defoln=0.000001):
    d11 = 0.0
    n = 2
    y = m.sin(n) / m.log(n, 2)
    
    while abs(y) >= defoln:
        d11 += y
        n += 1
        y = m.sin(n) / m.log(n, 2)
    
    return round(d11, 9)

try:
    cmd_vvod = input("Значение E: ")
    if cmd_vvod.strip() == "":
        otv = fnc2()
    else:
        defoln = float(cmd_vvod)
        otv = fnc2(defoln)
    
    print(f"Итог: {otv}")
except ValueError:
    print("Ошибка")'''

#1 (Арифметическое произведение)
def fnctn24(defoln=0.000001):
    sd = 1
    n = 2
    while True:
        nnn1 = 1 + 1 / (n * m.log(n))
        sd *= nnn1
        if abs(nnn1 - 1) < defoln:
            break
        n += 1
    return round(sd, 9)

pp = input("Значение E: ")
pp = float(pp) if pp else 0.000001

otv233 = fnctn24(pp)
print(otv233)

#2
def fnctn0(defoln=0.000001):
    sdd1 = 1
    n = 2
    while True:
        z = 1 + n / ((n - 1) * (n + 2))
        sdd1 *= z
        if abs(z - 1) < defoln:
            break
        n += 1
    return round(sdd1, 9)

vvod_1 = input("Значение E: ")
vvod_1 = float(vvod_1) if vvod_1 else 0.000001

otv_1 = fnctn0(vvod_1)
print(otv_1)

#3
def sc(defoln=0.000001):
    sdd1 = 1
    n = 1
    while True:
        z = 1 + (m.cos(n) / m.sin(n ** 2))
        sdd1 *= z
        if abs(z - 1) < defoln:
            break
        n += 1
    return round(sdd1, 9)

vvod_1 = input("Значение E: ")
vvod_1 = float(vvod_1) if vvod_1 else 0.000001

otv_3 = sc(vvod_1)
print(otv_3)

#4
def cvq(defoln=0.000001):
    sdd1 = 1
    n = 1
    while True:
        z = 1 + (m.atan(n) / (m.e**n - m.pi))
        sdd1 *= z
        if abs(z - 1) < defoln:
            break
        n += 1
    return round(sdd1, 9)

vvod_1 = input("Значение E: ")
vvod_1 = float(vvod_1) if vvod_1 else 0.000001

otv_3 = cvq(vvod_1)
print(otv_3)