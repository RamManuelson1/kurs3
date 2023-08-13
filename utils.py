import json
from datetime import datetime

def open_json(filename):

    """чтение данных из файла json"""

    with open(filename, 'r') as file:
        data = json.load(file)
        return data


def sort_transactions(transaction):

    """
    сортировка по датам
    """

    transactions = []
    for trans in transaction:
        if 'date' in trans:
            try:
                transactions.append(trans)
            except KeyError:
                continue
    sort_operations = sorted(transactions, key=lambda operation: datetime.fromisoformat(trans['date']), reverse=True)
    return sort_operations



def executed_operations(operations):

    """сортировка выполненных операций"""

    executed_operations = []
    for operation in operations:
        try:
            if operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
        except KeyError:
            continue
    return executed_operations[1:6]


def _5_executed_operations(operations_executed):
    """
    информация по 5-ти последним операциям
    """
    last_5_operations = ""
    for op in operations_executed:
        date_operation = op['date'][8:10] + '.' + op['date'][5:7] + '.' + op['date'][0:4]
        try:
            x = op['from']
            element_from = x[0:-16] + x[-16:-12] + " " + x[-12:-10] + "** *** " + x[-4:]
        except KeyError:
            element_from = "Неизвестно"
        element_to = "**" + op['to'][-4:]
        info_for_user = f''' 
        {date_operation} {op['description']}
        {element_from} -> {element_to}
        {op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}
        '''
        last_5_operations += info_for_user
    return last_5_operations