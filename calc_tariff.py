from decimal import Decimal


def calc_tariff(data: list):
    warehouse_costs = {}

    for order in data:
        warehouse_name = order['warehouse_name']
        highway_cost = Decimal(abs(order['highway_cost']))
        highway_cost_single = highway_cost / Decimal(len(order['products']))

        if warehouse_name in warehouse_costs:
            warehouse_costs[warehouse_name].append(highway_cost_single)
        else:
            warehouse_costs[warehouse_name] = [highway_cost_single]

    tariff_costs = {}

    for warehouse_name, costs in warehouse_costs.items():
        average_cost = Decimal(sum(costs)) / Decimal(len(costs))
        tariff_costs[warehouse_name] = average_cost.to_integral()

    return tariff_costs
