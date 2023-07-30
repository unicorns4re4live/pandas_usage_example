import pandas
from consts import TASK_5_FILE_NAME


def calculate_accumulated_percentage(file_path: str):
    df = pandas.read_excel(file_path)
    df = df.sort_values(by='percent_profit_product_of_warehouse', ascending=False)
    df['accumulated_percent_profit_product_of_warehouse'] = df['percent_profit_product_of_warehouse'].cumsum()
    df.to_excel(TASK_5_FILE_NAME, index=False)