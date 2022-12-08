# AccuKnox Assessment
#  - Siraj

import random

def restaurant_log():
    diner_food_items = {}

    # Read a Log file 
    with open("log.txt", "r") as f:
        for line in f:
            # getting the id values for 
            words = line.split(' ')
            print(f'Log: {line}')

            for w in words:
                if w.startswith('Eater_Id:'):
                    eater_id = w.split(':')[1]
                elif w.startswith('food_Id_log:'):
                    foodmenu_id = w.split(':')[1]

            if eater_id in diner_food_items:
                # After certain loops, the diner_food_items {} will be filled with data
                # then i'm checking the food_id is repeated more than once- yes : error | no : add new.
                # eg. --> {'2': ['4', '1'], '3': ['4'], '4': ['6']} -- Key is eater-id and list values are food-id.

                if foodmenu_id in diner_food_items[eater_id]:
                    print(
                        f"Error: Eater-ID: {eater_id} has already consumed food- FoodID: {foodmenu_id}.\n"
                    )
                else:
                    # Add the food item to the list of food items consumed by the diner
                    diner_food_items[eater_id].append(foodmenu_id)
            else:
                # Adding eater_id - key with values of food id - value.
                diner_food_items[eater_id] = [foodmenu_id]

    # Dictionary data which adds or count no. of times each diners consumed the food_id from here
    # we are goin to get the most food consumed or throws error if repeated.

    food_item_count = {}
    for food_items in diner_food_items.values():
        for food_item in food_items:
            if food_item in food_item_count:
                food_item_count[food_item] += 1
            else:
                food_item_count[food_item] = 1

    # Get the top 3 menu items consumed by eater_id(Diner).
    top_3_menu_items = sorted(food_item_count, key=food_item_count.get, reverse=True)[:3]
    print('\n')
    print(f"The Top 3 Delicious Food in the Menu or mostly liked Food Ids: {top_3_menu_items}")

def write_log(test_value):
    # test_value - no. of times we want to add logs.
    log = ''
    with open("log.txt", "w") as f:
        # Adding random elements to the logs by looping.
        for i in range(test_value):
            f.write(f'Date:{random.randrange(1,20)}-7-2022 Eater_Id:{random.randrange(1,5)}'
                    f' food_Id_log:{random.randrange(1,7)} cost: Rs.{random.randrange(100,500)}')
            f.write('\n')

def test_case():
    value = int(input('How many logs you want to add ? : -- \n'))
    print('\n')
    write_log(value)
    restaurant_log()

if __name__ == "__main__":
    test_case()
