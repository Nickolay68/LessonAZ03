import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100  # Количество точек
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Создание диаграммы рассеяния
plt.scatter(x, y, c='blue', alpha=0.5, edgecolors='w', s=50)

# Добавление заголовка и подписей к осям
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Показ графика
plt.show()