from utils import *
from utils import _5_executed_operations

file_json = 'operations.json'

def show_last_5_executed_operations():

    """вывод программы"""

    operation = open_json(file_json)
    executed_op = sort_transactions(operation)
    sorted_operations = executed_operations(executed_op)
    print(_5_executed_operations(sorted_operations))


if __name__ == "__main__":
    show_last_5_executed_operations()