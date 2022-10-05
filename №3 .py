'''Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля
и выводит свой результат в оценочной шкале от 1 до 5.
1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
3 - у пользователя в пароле соблюдается два условия из
      (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
4 - у пользователя в пароле соблюдается три условия из
      (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
5 - у пользователя есть цифры, буквы нижнего и верхнего регистра,
спец. символы и длинна пароля больше 8 символов'''


password = input('Введите пароль: ')

lower_list = "abcdefghijklmnopqrstuvwxyz"
digit_list = "1234567890"
upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spec_list = "#$%,&'()!*+,-./:;<=>?@[]^_`{|}~"

a = 0
b = 0
c = 0
d = 0

lent = 0
final_grade = 0

if len(password) > 8:
    lent = 1

for element in password:

    if element in lower_list:
        a = 1

    if element in digit_list:
        b = 1

    if element in upper_list:
        c = 1

    if element in spec_list:
        d = 1
s = a + b + c + d
if password == 'admin' or password == 'qwerty':
    final_grade = 1

elif s == 4 and lent == 1:
    final_grade = 5
elif s < 4:
    final_grade = s + 1
else:
    final_grade = 4

print(f'Сложность оценки:{final_grade}')

