import matplotlib.pyplot as plt

# Данные для аренды автомобилей
год = [2015, 2016, 2017, 2018, 2019]
renault = [10, 15, 17, 20, 21]
mersedes = [7, 7, 10, 18, 19]
bmw = [7, 10, 18, 25, 31]
hyundai = [2, 5, 18, 21, 25]

# Создание столбиковой диаграммы
plt.figure(figsize=(10, 6))
plt.bar(год, renault, color='b', width=0.4, label='Renault')
plt.bar(год, mersedes, color='r', width=0.4, label='Mersedes', bottom=renault)
plt.bar(год, bmw, color='g', width=0.4, label='BMW', bottom=[sum(x) for x in zip(renault, mersedes)])
plt.bar(год, hyundai, color='y', width=0.4, label='Hyundai', bottom=[sum(x) for x in zip(renault, mersedes, bmw)])

plt.xlabel('Год')
plt.ylabel('Количество арендованных автомобилей')
plt.title('Столбиковая диаграмма аренды автомобилей')
plt.legend()

plt.show()