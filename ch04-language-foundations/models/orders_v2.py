import datetime
from typing import List, Optional

from dateutil.parser import parse
from pydantic import BaseModel

order_json = {
    'item_id': '123',
    'created_date': '2002-11-24 12:22',
    'pages_visited': [1, 2, '3'],
    'price': 17.22
}


class Order(BaseModel):
    item_id: int
    created_date: Optional[datetime.datetime]
    pages_visited: List[int] = []
    price: float


o = Order(**order_json)
print(o)


# Default for JSON post
# Can be done for others with mods.
def order_api(order: Order):
    pass
