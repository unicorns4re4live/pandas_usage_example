import numpy as np
from consts import TASK_6_FILE_NAME
import pandas

def categorize_accumulated_percentage(file_path: str):
    df = pandas.read_excel(file_path)

    conditions = [
        (df['accumulated_percent_profit_product_of_warehouse'] <= 70),

        (df['accumulated_percent_profit_product_of_warehouse'] > 70)
        & (df['accumulated_percent_profit_product_of_warehouse'] <= 90)
    ]

    categories = ['A', 'B']
    default_category = 'C'

    df['category'] = pandas.Series(pandas.Categorical(np.select(conditions, categories, default_category)))
    df.to_excel(TASK_6_FILE_NAME, index=False)