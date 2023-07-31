import pandas
from decimal import Decimal
from consts import TASK_3_FILE_NAME


def calc_orders(data: list, warehouses_tariffs: dict):
    order_data = []

    for order in data:
        order_id = order['order_id']
        warehouse_name = order['warehouse_name']
        products = order['products']

        total_income = Decimal(0)
        total_expenses = Decimal(0)
        for product in products:
            price_per_unit = Decimal(product['price'])
            quantity = Decimal(product['quantity'])
            income = price_per_unit * quantity
            expense = warehouses_tariffs[warehouse_name] * quantity
            total_income += income
            total_expenses += expense

        order_profit = total_income - total_expenses

        order_data.append({
            'order_id': order_id,
            'order_profit': order_profit
        })

        df = pandas.DataFrame(order_data)

        average_profit = df['order_profit'].mean()

        average_profit_row = pandas.DataFrame({'order_id': ['Average Profit'], 'order_profit': [average_profit]})

        df = pandas.concat([df, average_profit_row], ignore_index=True)

        df.to_excel(TASK_3_FILE_NAME, index=False)