class MealTooBigError(Exception):
    """
    Raises an error if the input order contains more  than 2000 calories.
    """
    def __init__(self, calories):
        self.calories = calories
        self.message = f"Your meal is too big! {calories}  calories is too much!"
        super().__init__(self.message)