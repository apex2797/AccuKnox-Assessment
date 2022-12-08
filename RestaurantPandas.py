# AccuKnox Assessment
#  - Siraj

import datetime
import random
import time
import pandas as pd

# Expanding output table.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Creating a DataFrame locally. Lets assume its a Json, CSV or even DataBase.
df = pd.DataFrame({
'food_id':['B1', 'CF', 'C1', 'CF', 'B1', 'IO', 'B1', 'FT', 'BR','CF', 'C1', 'SM', 'IC','B1', 'SM'],
'purch_amt':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6, 500, 500, 250],
'ord_date': ['05-10-2022','09-10-2022','05-10-2022','08-17-2022','10-09-2022','07-27-2022','10-09-2022','10-10-2022','10-10-2022','06-17-2022','07-08-2022','04-25-2022','02-08-2022','08-08-2022','07-09-2022'],
'customer_id':['C31','C31','D35','D31','C35','D31','C35','D31','D35','C31','D35','D35','D35','C35','C38']})

# to get most of food ordered by the Diners.
def get_mostly_ordered_food_id():
    print('Max food_id ordered')
    # value_counts() gives us the repeated elements in the columns in order.
    # we can also try with groupby or agg.
    result = df['food_id'].value_counts().rename_axis('food_id').reset_index(name='counts')
    df2 = pd.DataFrame(result)
    print('\n------------- Top 3 Food Consumed ------------\n')
    # printing Top 3
    print(df2.head(3))

# just to show how many unique eater_id and Food_id we have.
def show_data():
    result = df.groupby(['customer_id'])
    print(result.first())

# Testing the Logs which adds entries in the Log(DataFrame).
def test_add_data():
    # getting no. of logs we want to add
    values_add = int(input('How many logs you want to enter? : '))
    foodID = ['B1', 'CF', 'C1', 'IO', 'FT', 'BR', 'IC', 'SM']
    customerID = ['C31','D35','D31','C35','C38']
    date = 'Test-Data'
    # looping into the range - and addign random elements to the dataframe.
    for i in range(values_add):
        df.loc[len(df.index)] = [random.choice(foodID), random.randrange(100,500), date, random.choice(customerID)]
    print('\n------------- Logs ------------\n')
    print(df)
    # calling the most_orderd function
    get_mostly_ordered_food_id()

def fav_food_consumed_by_customer(customer_id):
    # The input customer id but passing this value.
    # customer_id = "C31"

    # Select rows with the given customer id
    df_customer = df[df['customer_id'] == customer_id]

    # Get the list of unique food ids consumed by the customer
    food_ids = df_customer['food_id'].unique()
    print(f' ------------ CustomerID:{customer_id} - mostly consumed - {food_ids}')


def test_case():
    print(' Test Case \n')
    print('Adding Random logs to Logs.')
    time.sleep(1)
    test_add_data()
    customerID = ['C31', 'D35', 'D31', 'C35', 'C38']
    print("\n------------- Customer's favourite Food Ids ------------\n")

    # calling the function by passing the customer id params in a loop.
    for i in customerID:
        fav_food_consumed_by_customer(i)


if __name__ == "__main__":
    test_case()
