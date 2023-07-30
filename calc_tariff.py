def calc_tariff(data: list):
    warehouse_costs = {}

    for order in data:
        warehouse_name = order['warehouse_name']
        highway_cost = abs(order['highway_cost'])
        highway_cost_single = highway_cost / len(order['products'])

        if warehouse_name in warehouse_costs:
            warehouse_costs[warehouse_name].append(highway_cost_single)
        else:
            warehouse_costs[warehouse_name] = [highway_cost_single]

    tariff_costs = {}

    for warehouse_name, costs in warehouse_costs.items():
        average_cost = sum(costs) / len(costs)
        tariff_costs[warehouse_name] = round(average_cost)

    return tariff_costs
