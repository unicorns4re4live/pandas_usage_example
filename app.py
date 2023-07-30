import json
from consts import DATASET_FILE_NAME, TASK_2_FILE_NAME, TASK_3_FILE_NAME, \
    TASK_4_FILE_NAME, TASK_5_FILE_NAME, TASK_6_FILE_NAME

from calc_accumulated_percentage import calculate_accumulated_percentage
from categorize_accumulated_percentage import categorize_accumulated_percentage
from calc_income_percentage import calc_income_percentage
from calc_orders import calc_orders
from calc_tariff import calc_tariff
from calc_summary import calc_summary

with open(DATASET_FILE_NAME, encoding='utf-8') as data_file:
    data = json.load(data_file)

task_1_result = calc_tariff(data=data)
print('Task 1 result:', task_1_result)

calc_summary(data=data, warehouses_tariffs=task_1_result)
print(f'Task 2 result is in {TASK_2_FILE_NAME}')

calc_orders(data=data, warehouses_tariffs=task_1_result)
print(f'Task 3 result is in {TASK_3_FILE_NAME}')

calc_income_percentage(data=data, warehouses_tariffs=task_1_result)
print(f'Task 4 result is in {TASK_4_FILE_NAME}')


calculate_accumulated_percentage(file_path=TASK_4_FILE_NAME)
print(f'Task 5 result is in {TASK_5_FILE_NAME}')

categorize_accumulated_percentage(file_path=TASK_5_FILE_NAME)
print(f'Task 6 result is in {TASK_6_FILE_NAME}')



