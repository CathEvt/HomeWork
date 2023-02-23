chislo = int(input('Введите число '))
if 100<=chislo<1000:
    sum = int(str(chislo)[0]) + int(str(chislo)[1]) + int(str(chislo)[2])
    pro = int(str(chislo)[0]) * int(str(chislo)[1]) * int(str(chislo)[2])
    print('Сумма чисел: ' + str(sum), 'Произведение чисел: ' + str(pro))
else:
    print('Число не трехзначное')