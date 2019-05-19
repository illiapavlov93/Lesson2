a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Enter number')
b = int(input())

n = len(a) - 1
c = 0

while c <= n:
    e = (c + n) // 2
    if b < a[e]:
        n = e - 1
    elif b > a[e]:
        c = e + 1
    else:
        print(e)
        break
else:
    print("No the number")
