import pandas
from consts import TASK_2_FILE_NAME


def calc_summary(data: list, warehouses_tariffs: dict):
    product_data = []

    for order in data:
        warehouse_name = order['warehouse_name']
        products = order['products']

        for product in products:
            product_name = product['product']
            price_per_unit = product['price']
            quantity = product['quantity']

            income = price_per_unit * quantity
            expense = warehouses_tariffs[warehouse_name] * quantity
            profit = income - expense

            existing_product = next((item for item in product_data if item['Product'] == product_name), None)

            if existing_product:
                existing_product['Quantity'] += quantity
                existing_product['Income'] += income
                existing_product['Expenses'] += expense
                existing_product['Profit'] += profit
            else:
                product_data.append({
                    'Product': product_name,
                    'Quantity': quantity,
                    'Income': income,
                    'Expenses': expense,
                    'Profit': profit
                })

    df = pandas.DataFrame(product_data)
    df.to_excel(TASK_2_FILE_NAME, index=False)

    return product_data
