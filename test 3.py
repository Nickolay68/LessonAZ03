import matplotlib
import pandas
import BeautifulSoup
import requests

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с диванами
url = 'https://www.divan.ru/category/divany'

# Получение HTML содержимого страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Извлечение данных о диванах
sofa_data = []
for item in soup.find_all('div', class_='product-card'):
    try:
        name = item.find('a', class_='product-card__name').text.strip()
        price = item.find('span', class_='product-card__price').text.strip()
        # Удаляем символы валюты и пробелы
        price = int(price.replace('₽', '').replace(' ', ''))
        sofa_data.append({'name': name, 'price': price})
    except AttributeError:
        continue

# Создание DataFrame и сохранение в CSV
df = pd.DataFrame(sofa_data)
df.to_csv('sofa_prices.csv', index=False)

# Вычисление средней цены
average_price = df['price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Построение гистограммы
plt.hist(df['price'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.show()