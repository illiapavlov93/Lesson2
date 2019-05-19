a = "English = 78 Science = 83 Math = 68 History = 65"
b = a.split()
n = 0
for i in b:
    if i.isdigit():
        n += int(i)
print(n)
