import pandas
from decimal import Decimal
from consts import TASK_4_FILE_NAME


def percent_profit_product_of_warehouse(row: dict, warehouse_profits: dict):
    warehouse_profit = warehouse_profits[row['warehouse_name']]
    product_profit = Decimal(row['profit'])
    return (product_profit / warehouse_profit) * Decimal(100)


def calc_income_percentage(data: list, warehouses_tariffs: dict):
    warehouse_product_data = []

    for order in data:
        warehouse_name = order['warehouse_name']
        products = order['products']

        for product in products:
            product_name = product['product']
            price_per_unit = Decimal(product['price'])
            quantity = Decimal(product['quantity'])

            income = price_per_unit * quantity
            expense = warehouses_tariffs[warehouse_name] * quantity
            profit = income - expense

            warehouse_product_data.append({
                'warehouse_name': warehouse_name,
                'product': product_name,
                'quantity': quantity,
                'profit': profit
            })

    df = pandas.DataFrame(warehouse_product_data)
    df = df.groupby(['warehouse_name', 'product'], as_index=False).agg({'quantity': 'sum', 'profit': 'sum'})

    warehouse_profits = df.groupby('warehouse_name')['profit'].sum()

    df['percent_profit_product_of_warehouse'] = df.apply(
        lambda row: percent_profit_product_of_warehouse(row, warehouse_profits),
        axis=1
    )

    df.to_excel(TASK_4_FILE_NAME, index=False)
