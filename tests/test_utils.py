from utils import sort_transactions, _5_executed_operations

def test_sort_transactions():
    assert sort_transactions([]) == []


def test__5_executed_operations():
    assert _5_executed_operations([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]) != ""