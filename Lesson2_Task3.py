print('Введите строку')
a = input()
b = list(a)
c = b[::-1]

if b == c:
    print('Палиндром')
else:
    print('Не палиндром')
