"""
Написать программу на языке Prolog для вычисления суммы
элементов списка. На вход подаётся целочисленный массив.
На выходе - сумма элементов массива.
"""
from pyswip import Prolog

prolog = Prolog()
prolog.consult("sum_list.pl")

input_array = [1, 2, 3, 4, 5]
query = f"sum_list({input_array}, X)."
result = list(prolog.query(query))
sum_result = result[0]['X'] if result else None

print(f"Сумма элементов списка {input_array}: {sum_result}")
