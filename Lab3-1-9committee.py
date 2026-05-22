import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. Загрузка данных из statsmodels
data = sm.datasets.committee.load_pandas().data

# 2. Выбор факторов
# Факторы: BILLS104 (ось X) и SIZE (ось Y)
# Классы: PRESTIGE (цветовая шкала)
x = data['BILLS104']
y = data['SIZE']
classes = data['PRESTIGE']

# 3. Построение диаграммы
plt.figure(figsize=(10, 6))

# scatter: c=classes задает цвет согласно уровню престижа
scatter = plt.scatter(x, y, c=classes, cmap='coolwarm', s=100, edgecolors='k')

# Добавление легенды (Colorbar для количественных данных)
cbar = plt.colorbar(scatter)
cbar.set_label('Prestige Level')

# Подписи осей и заголовок
plt.xlabel('BILLS104')
plt.ylabel('SIZE')
plt.title('Диаграмма рассеяния: Committee Dataset')
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
