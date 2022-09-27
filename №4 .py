"""Напишите программу где пользователь вводит число symbol_len,
а программа генерирует пароль длинной symbol_len.
Чем выше будет сложность пароля, тем лучше.
Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3"""

import random

chars = "+-/*!&$#?''=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
symbol_len = int(input(' Длина строки : '))
psw = ''
for i in range(symbol_len):
    psw += random.choice(chars)

print(psw)
