import requests
from bs4 import BeautifulSoup


globus_url = 'https://globus-online.kg'
response = requests.get('https://globus-online.kg/catalog/')
soup = BeautifulSoup(response.text, 'html.parser')

result = []
categories = soup.findAll('a', {'class': 'around_image'})

for category in categories:
    response = requests.get(f'{globus_url}{category.get("href")}')
    soup = BeautifulSoup(response.text, 'html.parser')
    sub_categories = soup.findAll('a', {'class': 'clearfix'})
    sub_result = []
    for sub_category in sub_categories:
        sub_result.append({
            'name': sub_category.span.get_text(),
            'products_url': sub_category.get('href')
        })
    result.append({
        'name': category.img.get('title'),
        'img': category.img.get('src'),
        'sub_categories': sub_result
    })


print('Категории товаров GLOBUS')
print('--------------------------')
for category in result:
    print(f'Название: {category["name"]}')
    print(f'Путь до картинки: {category["img"]}')
    print(f'под категории:')
    for sub_category in category['sub_categories']:
        print(f'\tНазвание: {sub_category["name"]}')
        print(f'\tСсылка к продутам: {sub_category["products_url"]}')
    print('------------------------------')
