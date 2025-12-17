# Задание 3
world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

# 2022 год
world_champions[2022] = 'Аргентина'

# Чемпионы в формате "год - страна"
for year, country_name in world_champions.items():
    print(year, '-', country_name)

country = 'Италия'

# 3. Проверка на победу Италии
if country in world_champions.values():
    print(country, 'становилась чемпионом мира по футболу в 21 веке!')
else:
    print(country, 'не выигрывала чемпионат мира по футболу в 21 веке')
