import json
from datetime import datetime

def mask_card(card_number):

    """принимает номер карты и замаскирует его, оставляя только первые 6 и последние 4 цифры"""

    masked_card = f"{card_number[:6]}{'*' * 6}{card_number[-4:]}"
    return masked_card

def mask_account(account_number):

    """принимает номер счета и замаскирует его, оставляя только последние 4 цифры"""

    masked_account = f"**{account_number[-4:]}"
    return masked_account

def format_operation(operation):

    """принимает операцию и форматирует ее данные"""

    date = datetime.strptime(operation['date'], '%d.%m.%Y').strftime('%d.%m.%Y')
    description = operation['description']
    from_account = mask_card(operation.get('from', ''))
    to_account = mask_account(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']

    formatted_operation = f"{date} {description}\n{from_account} -> {to_account}\n{amount} {currency}\n"
    return formatted_operation

def print_last_5_operations(operations):

    """принимает список операций и выводит на экран отформатированные данные для последних 5 операций"""

    last_5_operations = operations[:5]
    formatted_operations = [format_operation(operation) for operation in last_5_operations]
    print('\n'.join(formatted_operations))

def main():

    """открывается файл с данными операций, фильтруются и сортируются выполненные операции,
    а затем вызывается функция `print_last_5_operations` для вывода результатов."""

    with open('operations.json', 'r') as file:
        data = json.load(file)

    executed_operations = list(filter(lambda operation: operation['date'] == 'EXECUTED', data))
    sorted_operations = sorted(executed_operations, key=lambda operation: datetime.strptime(operation['date'], '%d.%m.%Y'), reverse=True)

    print_last_5_operations(sorted_operations)

if __name__ == '__main__':
    main()