import datetime

from dateutil.parser import parse

order_json = {'item_id': '123', 'created_date': '2002-11-24 12:22', 'pages_visited': [1, 2, '3'], 'price': 17.22}


# class Order:
#
#     def __init__(self, item_id: int, created_date: datetime.datetime,
#                  pages_visited: list[int], price: float):
#         self.item_id = item_id
#         self.created_date = created_date
#         self.pages_visited = pages_visited
#         self.price = price
#
#     def __str__(self):
#         return str(self.__dict__)


class Order:
    def __init__(self, item_id: int, created_date: datetime.datetime, price: float, pages_visited=None):
        if pages_visited is None:
            pages_visited = []

        try:
            self.item_id = int(item_id)
        except ValueError:
            raise Exception('Invalid item_id, it must be an integer.')

        try:
            self.created_date = parse(created_date)
        except:
            raise Exception('Invalid created_date, it must be an datetime.')

        try:
            self.price = float(price)
        except ValueError:
            raise Exception('Invalid price, it must be an float.')

        try:
            self.pages_visited = [int(p) for p in pages_visited]
        except:
            raise Exception('Invalid page list, it must be iterable and contain only integers.')

    def __str__(self):
        return (
            f'item_id={self.item_id}, created_date={repr(self.created_date)}, '
            f'price={self.price}, pages_visited={self.pages_visited}'
        )

    def __eq__(self, other):
        return isinstance(other, Order) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return isinstance(other, Order) and self.__dict__ != other.__dict__


o = Order(**order_json)
print(o)
