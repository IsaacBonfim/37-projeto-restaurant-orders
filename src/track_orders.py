from .analyze_log import create_orders_lists, clients_info


class TrackOrders:
    def __init__(self) -> None:
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        self.__orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        days, clients, products = create_orders_lists(self.__orders)
        clients_set = clients_info(self.__orders, days, clients, products)

        clients_orders = clients_set[customer]["orders"]
        order_qnt = 0
        ordered_prod = ""

        for order, qnt in clients_orders.items():
            if qnt > order_qnt:
                order_qnt = qnt
                ordered_prod = order

        return ordered_prod

    def get_never_ordered_per_customer(self, customer):
        days, clients, products = create_orders_lists(self.__orders)
        clients_set = clients_info(self.__orders, days, clients, products)

        clients_orders = clients_set[customer]["orders"]
        never_ordered = []

        for order, qnt in clients_orders.items():
            if not qnt:
                never_ordered.append(order)

        return set(never_ordered)

    def get_days_never_visited_per_customer(self, customer):
        days, clients, products = create_orders_lists(self.__orders)
        clients_set = clients_info(self.__orders, days, clients, products)

        clients_days = clients_set[customer]["days"]
        never_visited = []

        for order, qnt in clients_days.items():
            if not qnt:
                never_visited.append(order)

        return set(never_visited)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
