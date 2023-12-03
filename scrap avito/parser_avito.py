import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_avito_data():
    url = 'https://www.avito.ru'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Ищем все блоки с объявлениями
    items = soup.find_all('li', class_='css-1dbjc4n e1qqw7js')

    data = []
    for item in items:
        title = item.a.string
        price = item.find('span', class_='css-901oao e1b8d8b3').string
        link = item.a['href']
        data.append({
            'Title': title,
            'Price': price,
            'Link': link
        })
    return data


data = get_avito_data()

# Создаем DataFrame
df = pd.DataFrame(data)

writer = pd.ExcelWriter('avito_data.xlsx')
df.to_excel(writer, index=False, header=True)
writer.save()
writer.close()
