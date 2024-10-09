import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline as spline
import numpy as np

# Переменные координат точек по x
x1 = 2
x2 = 3
x3 = 4

print("Введите x1")
x1=int(input())
print("Введите x2")
x2=int(input())
print("Введите x3")
x3=int(input())

# Переменные координат точек по y
y1 = 0
y2 = 3
y3 = 1

print("Введите y1")
y1=int(input())
print("Введите y2")
y2=int(input())
print("Введите y3")
y3=int(input())



print("Координаты")
print(f"x: {x1} {x2} {x3}")
print(f"y: {y1} {y2} {y3}")


print("Высчитываем полином Лагранжа L2")

L2 = ""
if y1 != 0:
    L2 += f"{y1}*l1(x)"
if y2 != 0:
    if y2 > 0: L2 += f"+"
    L2 += f"{y2}*l2(x)"
if y3 != 0:
    if y3 > 0: L2 += "+"
    L2 += f"{y3}*l3(x)"

if L2[0] == "+":
    L2 = L2[1:]

print(f"L2=y1*l1(x)+y2*l2(x)+y3*l3(x)={L2}")

print("\n")
print("Высчитываем фундоментальные полиномы Лагранжа")
L2+="="
l1=l2=l3=""
if y1 != 0:
    l1 = f"x^2-({x2 + x3})x+{x2 * x3}/{(x1 - x2) * (x1 - x3)}"
    print(f"l1={l1}")

if y2 != 0:
    l2 = f"x^2-({x1 + x3})x+{x1 * x3}/{(x2 - x1) * (x2 - x3)}"
    print(f"l2={l2}")

if y3 != 0:
    l3 = f"x^2-({x1 + x2})x+{x1 * x2}/{(x3 - x1) * (x3 - x2)}"
    print(f"l3={l3}")

print(f"\nИтого полином Лагранжа \nL2(x)={y1}*({l1})+{y2}*({l2})+{y3}*({l3})")

print("\n \n Полином по Ньютону")

delta12 = (y1 - y2) / (x1 - x2)
print(f"Дельта 1 (1,2) = {delta12}")

delta23 = (y2 - y3) / (x2 - x3)
print(f"Дельта 1 (2,3) = {delta23}")

delta123 = (delta12 - delta23) / (x1 - x3)
print(f"Дельта 2 (1,2,3) = {delta123}")

N2 = f"N2={delta123}x^2+{delta12 - (delta123 * (x1 + x2))}x+({y1 - (delta12 * x1) + (delta123*(x1 * x2))})"
print(N2)


#Изначальные точки
X = [x1, x2, x3]
Y = [y1, y2, y3]

#Постоение графика по точкам
plt.plot(X, Y)
plt.title("График интерполяционного полинома")
plt.xlabel("X")
plt.ylabel("Y")
#Построение графика для полиномов Ньютона и Лагранжа

xnew = np.linspace(x1, x3, 30)
spl = spline(X, Y, 2)
ynew = spl(xnew)
plt.plot(xnew, ynew)

#Прописываем наименование графиков
plt.legend(["График по точкам", "Полиномы Ньютона и Лагранжа"])
plt.show()
