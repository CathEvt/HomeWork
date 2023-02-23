per = int(input('Введите число '))
m = per%10
per = per//10
while per > 0:
    if per%10 > m:
        m = per%10
    per = per//10
print(m)