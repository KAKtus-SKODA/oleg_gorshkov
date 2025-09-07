Dictionary_1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Dictionary_2 = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(state: str) -> dict:
    '''  функция которая принимает список словарей и опционально значение для ключа 
         state (по умолчанию 'EXECUTED' ). Функция возвращает новый список словарей, 
         содержащий только те словари, у которых ключ state соответствует указанному значению.'''
    if list_state = 'EXECUTED':
        print(Dictionary_1)
    elif list_state = 'CANCELED':
        print(Dictionary_2)
    return list_state


def sort_by_date(date: list): -> list:
    '''функцию sort_by_date , которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).'''
    date_sorted = sorted(date, key=lambda x: x['date'], reverse=True)
    return date_sorted

date_sorted_rezultat = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print(date_sorted_rezultat)
