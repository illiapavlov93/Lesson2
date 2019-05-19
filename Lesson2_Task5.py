import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''
a = ''
while a is not int:
    try:
        a = int(input('Длина пароля?'))
        break
    except ValueError:
        print('Введите корректную длину пароля')

if a == 0:
    print('Вы указали длину пароля равной 0')
else:
    for i in range(a):
        password += random.choice(chars)

print(password)
