per = int(input('Введите число '))
a = 1
faktorial = 1
while a <= per:
    faktorial *= a
    a += 1
print('Факториал чтсла', per, 'равен', faktorial)
