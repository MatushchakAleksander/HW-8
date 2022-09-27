"""Написать программу, которая проверяет,
что в строке есть хотя бы один пробел, число,
буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'"""

text = "Hello world 2023"
text_space = text_digit = text_upper = text_lower = 0

for element in text:
    if element.isspace():
        text_space = 1

    if element.isdigit():
        text_digit = 1

    if element.isupper():
        text_upper = 1

    if element.islower():
        text_lower = 1

if text_space and text_digit and text_upper and text_lower:

    print('YES')
else:
    print('NO')

# "Helloworld2023"   >>> NO
# "Hello world "     >>> NO
# "hello world 2023" >>> NO
# "HELLO WORLD 2023" >>> NO
