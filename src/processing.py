Dictionary_1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Dictionary_2 = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(state: str) -> dict:
    '''  функция которая принимает список словарей и опционально значение для ключа
         state (по умолчанию 'EXECUTED' ). Функция возвращает новый список словарей,
         содержащий только те словари, у которых ключ state соответствует указанному значению.'''
    if state == 'EXECUTED':
        print(Dictionary_1)
    elif state == 'CANCELED':
        print(Dictionary_2)
    return state


def sort_by_date(banking_operation, reverse=True):
    '''Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате.'''
    return sorted(banking_operation, key=lambda x: x.get('date'), reverse=reverse)
