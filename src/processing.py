from typing import List, Dict
from datetime import datetime


""" Обработка ключей """


def filter_by_state(banking_operations: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """ Функция принимает на вход список словарей с данными о банковских операциях и параметр state,
     возвращает новый список, содержащий только те словари,
      у которых ключ state содержит переданное в функцию значение """
    return [operation for operation in banking_operations if operation.get('state') == state]


""" Сортировка данных """


def sort_by_date(banking_operation: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """ Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате """
    return sorted(banking_operation, key=lambda x: datetime.fromisoformat(x['date']))
