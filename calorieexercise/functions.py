
from constants import calories, combos
from classes import MealTooBigError 

def calorie_counter(order):
    total_calories=0
    for item in order:
        total_calories = total_calories + calories[item]
    return total_calories

def calorie_counter_with_args(*order):
    x=0
    for i in order:
        x = x + calories[i]
    return x

def combo_calories_counter (ordered_item):
    total_calories=0
    for item in ordered_item:
        if item in calories:
           total_calories= total_calories + calories[item]
        elif item in  combos:
            combo_items= combos[item]
            total_calories= total_calories + sum(calories[item]for item in combo_items)
        else:
            print(f"the {item}is not in the calorie database or is not a valid combo.")
    return total_calories

def combo_calories_counter_with_key_error (ordered_item):
    total_calories=0
    for item in ordered_item:
        if item in calories:
            total_calories= total_calories + calories[item]
        else:
            try:
                combo_items= combos[item]
                total_calories= total_calories + sum(calories[item]for item in combo_items)
            except KeyError:
                print(f"The {item} is not on the menu.")
    return total_calories

def calculate_total_price(ordered_items, meals_dict, combos_dict):
    total_price = 0
    for item in ordered_items:
        try:
            if item in meals_dict:
                total_price += meals_dict[item]["price"]
            elif item in combos_dict:
                total_price += combos_dict[item]["price"]
            else:
                raise KeyError
        except KeyError:
            print(f"{item} is not in the menu.")
    return total_price


def calories_counter_with_exception (ordered_item):
    total_calories=0
    for item in ordered_item:
        if item in calories:
           total_calories= total_calories + calories[item]
        elif item in  combos:
            combo_items= combos[item]
            total_calories= total_calories + sum(calories[item]for item in combo_items)
        else:
            print(f"the {item}is not in the calorie database or is not a valid combo.")
    if total_calories > 2000:
        raise MealTooBigError(total_calories)
    return total_calories







