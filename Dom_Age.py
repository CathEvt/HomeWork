n=int(input("Введите Ваш возраст:"))
if n<=0 or n>=100:
    print("Возраст не соответсвует")
elif 5<=n<=20 or n%10==0 or n%10>=5:
    print("Вам", n, "лет")
elif n==1 or n%10==1:
    print("Вам",n,"год")
else:
    print("Вам",n,"года")
