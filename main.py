geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def remove_some_country(country):
    for items in geo_logs:
        values = items.values()
        for item in values:
            if country not in item:
                geo_logs.remove(items)
                remove_some_country(country)
    return geo_logs

remove_some_country('Россия')
print(geo_logs)

def get_unic_values():
    temp_list = []
    for items in ids.values():
        temp_list += items

    unic_values = list(set(temp_list))
    return unic_values

get_unic_values()

##

