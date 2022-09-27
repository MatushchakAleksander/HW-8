""" Напишите программу, где пользователь вводит пароль,
а программа проверяет сложность пароля и выводит свой результат
в оценочной шкале от 1 до 5.
a.1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
b.2 - у пользователя все буквы в нижнем регистре
c.3 - у пользователя есть буквы в нижнем регистре
d.4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
e.5 – у пользователя есть цифры, буквы нижнего и верхнего регистра,
      спец. символы и длинная пароля больше 8 символов."""

password = input('Введите пароль: ')

lower_list = "abcdefghijklmnopqrstuvwxyz"
digit_list = "1234567890"
upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spec_list = "#$%&'()!*+,-./:;<=>' '?@[]^_`{|}~"

a = 0
b = 0
c = 0
d = 0

lent = 0
final_grade = 0

for element in password:

    if len(password) > 8:
        lent = 1

    if element in lower_list:
        a = 1

    if element in digit_list:
        b = 1

    if element in upper_list:
        c = 1

    if element in spec_list:
        d = 1

final_grade = a + b + c + d + lent
print(final_grade)
