import matplotlib.pyplot as plt
y = []
H = []
P = []
T = []
with open("HPTValues.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for l in lines[:-1]:
        H.append(float(l[13:18]))
        P.append(float(l[34:40]))
        T.append(float(l[54:59]))
x = lines[-1].split()
for i in range(len(x)):
    x[i] = float(x[i])

y1 = H
y2 = P
y3 = T

# 1. Создание рисунка и осей
fig, axs = plt.subplots(3, 1)  # 3 строки, 1 столбец

axs[0].plot(x, y1)
axs[0].set_title("Humidity, %")

axs[1].plot(x, y2)
axs[1].set_title("Pressure, Pa")

axs[2].plot(x, y3)
axs[2].set_title("Temperature, C")

for i in range(3):
    axs[i].grid(which='major', linewidth=1)
    axs[i].grid(which='minor', linewidth=0.5, linestyle='-.')
    axs[i].minorticks_on()

#Автоматическая настройка расположения графиков
plt.tight_layout()

plt.show()

print("x:", x)
print("H:", H)
print("P:", P)
print("T:", T)