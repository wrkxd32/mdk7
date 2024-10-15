# 1
def describe_shape(shape):
    match shape:
        case "квадрат":
            return "У квадрата 4 стороны"
        case "треугольник":
            return "У треугольника 3 стороны"
        case "круг":
            return "У круга нет сторон"
        case _:
            return "Неизвестная фигура"

# 2
def classify_number(num):
    match num:
        case n if n > 0:
            return "Положительное число"
        case n if n < 0:
            return "Отрицательное число"
        case 0:
            return "Ноль"

# 3
def day_of_week(day):
    match day:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "Некорректный номер дня"

# 4
def analyze_list(nmbs):
    match nmbs:
        case []:
            return "Список пуст."
        case [num]:
            return f"В списке одно число: {num}"
        case [num1, num2]:
            return f"В списке два числа: {num1} и {num2}"
        case _:
            return f"В списке много чисел, всего: {len(nmbs)}"

# 5
def get_animal_sound(sn):
    sounds = {
        "кот": "мяу",
        "собака": "гав",
        "корова": "му"
    }
    
    match sn:
        case a if a in sounds:
            return sounds[a]
        case _:
            return "Неизвестно"

print(get_animal_sound("кот"))
print(get_animal_sound("тигр"))
print(get_animal_sound("собака"))