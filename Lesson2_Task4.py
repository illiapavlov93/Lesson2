print('Введите строку')
a = input()
b = list(a)
b.append(' ')
c = []
d = []
e = []
for i in b:
    if i is not ' ':
        d.append(i)
    else:
        d.append(i)
        e = d[::-1]
        c.extend(e)
        d = []
c.remove(' ')
print(''.join(map(str, c)))

