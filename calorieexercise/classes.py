
from exceptions import MealTooBigError
from functions import calories_counter_with_exception



class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(self, items, date=None):
        Order.counter += 1
        self.order_id = Order.counter
        self.order_accepted = True
        self.order_refused_reason = ''
        self.date = date
        self.items = items
        calories = self.calories
        if calories > 2000:
            raise MealTooBigError(calories)
        

    @property
    def calories(self):
        test = self.calories_counter_with_exception(self.items, i=0, total_calories=0)
        return test