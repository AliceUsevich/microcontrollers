import matplotlib.pyplot as plt
import numpy as np

y = []
with open("Volues.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for l in lines[:-1]:
        y.append(float(l[2:-6]))
x = lines[-1].split()
for i in range(len(x)):
    x[i] = float(x[i])
print("x:", x)
print("y:", y)
plt.plot(x, y)
plt.show()