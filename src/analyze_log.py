import csv


def create_orders_lists(data):
    days = []
    clients = []
    products = []

    for name, order, day in data:
        if day not in days:
            days.append(day)

        if name not in clients:
            clients.append(name)

        if order not in products:
            products.append(order)

    return [set(days), set(clients), set(products)]


def clients_info(data, days, clients, products):
    orders = {
        client: {
            'orders': {
                product: 0 for product in products
            },
            'days': {
                day: 0 for day in days
            }
        } for client in clients
    }

    for name, order, day in data:
        orders[name]['orders'][order] += 1
        orders[name]['days'][day] += 1

    return orders


def maria_info(obj):
    most_orders_maria = ''
    most_orders_maria_qnt = 0

    for order, qnt in obj['orders'].items():
        if qnt > most_orders_maria_qnt:
            most_orders_maria = order
            most_orders_maria_qnt = qnt

    return most_orders_maria


def joao_info(obj):
    never_ordered = []
    never_went = []

    for order, qnt in obj['orders'].items():
        if not qnt:
            never_ordered.append(order)

    for day, qnt in obj['days'].items():
        if not qnt:
            never_went.append(day)

    return [set(never_ordered), set(never_went)]


def save_info(maria, arnaldo, joao_prod, joao_days):
    with open('data/mkt_campaign.txt', 'w') as file:
        string_to_write = f'{maria}\n{arnaldo}\n{joao_prod}\n{joao_days}'
        file.write(string_to_write)


def analyze_log(path_to_file):

    if '.csv' not in path_to_file:
        raise FileNotFoundError(f'Extensão inválida. {path_to_file}')

    try:
        with open(path_to_file) as file:
            info = csv.reader(file)
            data = [item for item in info]

            days, clients, products = create_orders_lists(data)
            orders = clients_info(data, days, clients, products)

            most_ordered_maria = maria_info(orders['maria'])
            hamburguer_arnaldo = orders['arnaldo']['orders']['hamburguer']
            joao_never_ordered, joao_never_went = joao_info(orders['joao'])
            
            save_info(
                most_ordered_maria,
                hamburguer_arnaldo,
                joao_never_ordered,
                joao_never_went
            )
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente. {path_to_file}')
