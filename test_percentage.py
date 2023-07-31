import pandas as pd

from consts import TASK_4_FILE_NAME, TASK_5_FILE_NAME, TASK_6_FILE_NAME


def test_total_profits():
    df = pd.read_excel(TASK_4_FILE_NAME)

    warehouse_percent_profits = df.groupby('warehouse_name')['percent_profit_product_of_warehouse'].sum()

    for warehouse, total_profit in warehouse_percent_profits.items():
        assert total_profit == 100, f"Total profit for warehouse '{warehouse}' is not equal to 100."


def test_accumulated_percentage():
    df = pd.read_excel(TASK_5_FILE_NAME)

    for i in range(1, len(df)):
        prev_accumulated = df.at[i - 1, 'accumulated_percent_profit_product_of_warehouse']
        current_percent = df.at[i, 'percent_profit_product_of_warehouse']
        current_accumulated = df.at[i, 'accumulated_percent_profit_product_of_warehouse']

        expected_accumulated = prev_accumulated + current_percent

        assert round(current_accumulated, 6) == round(expected_accumulated, 6), f"Accumulated percentage mismatch at row {i + 1}."


def test_category_assignment():
    df = pd.read_excel(TASK_6_FILE_NAME)

    for i in range(len(df)):
        accumulated_percent = df.at[i, 'accumulated_percent_profit_product_of_warehouse']
        category = df.at[i, 'category']

        if accumulated_percent <= 70:
            expected_category = 'A'
        elif 70 < accumulated_percent <= 90:
            expected_category = 'B'
        else:
            expected_category = 'C'

        assert category == expected_category, f"Category mismatch at row {i + 1}."
