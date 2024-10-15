#1
user = input("Введите ваше имя: ")
with open('guest.txt', 'w', encoding='utf-8') as file:
    file.write(user + '\n')

#2
with open('guest_book.txt', 'a') as file:
    while True:
        user = input("Ваше имя: ")
        if user.lower() == 'выход':
            break
        print(f"Приветствую, {user}")
        file.write(f"Привет, {user}\n")

#3
with open('save.txt', 'a') as file:
    while True:
        ww = input("Почему вам нравится программировать?: ")
        if ww.lower() == 'выход':
            break
        file.write(ww + '\n')