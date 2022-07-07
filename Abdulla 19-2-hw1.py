osh = float(input('Введите температуру в Ош:'))
chui = float(input('Введите температуру в Чуй:'))
batken = float(input('Введите температуру в Баткен:'))
naryn = float(input('Введите температуру в Нарын:'))
talas = float(input('Введите температуру в Талас:'))
djalabad = float(input('Введите температуру в Джалал-Абад:'))
yssykol = float(input('Введите температуру в Ыссык-Кол:'))
kyrg = osh+chui+batken+naryn+talas+djalabad+yssykol
print(kyrg)
kyrgtemp = kyrg/7
print(round(kyrgtemp ,1))
