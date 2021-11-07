# -*- coding: utf-8 -*-

"""
    Pandas Exercise
    Using Chipotle dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
chipotle = pd.read_csv('H:/ML Projects/Pandas/chipotle.tsv', sep='\t')
chipotle.head(10)
chipotle.info()

# Which was the most ordered item?
chipotle['item_name'].value_counts().head(1)

# Which was the most ordered item in the choice description section?
chipotle['choice_description'].value_counts().head(1)

# How many items were ordered in total?
sum(chipotle['item_name'].value_counts())

# Turn the item prices into float
chipotle.item_price.dtype
chipotle.item_price = chipotle.item_price.apply(lambda x: float(x[1:]))
chipotle.item_price.dtype

# What was the total revenue?
r = sum(chipotle.item_price*chipotle.quantity)
print("Total Revenue = $" + str(np.round(r, 2)))

# How many orders were made?
chipotle.order_id.max()

# What was the average revenue per order?
chipotle['Revenue'] = chipotle['item_price'] * chipotle['quantity']
r = chipotle.groupby('order_id').sum().mean()['Revenue']
print("Average Revenue per order = $" + str(np.round(r, 2)))

# How many different items were sold?
chipotle['item_name'].nunique() 

# What are the average number of toppings per burrito?
avg_top = {}
top_count = {}
burrito_count = {}
for item in chipotle.drop_duplicates().item_name:
    if "Burrito" in item:
        itemsdf = chipotle[chipotle.item_name==item]
        burrito_count[item] = len(itemsdf.index)
        sum = 0
        for i in itemsdf.choice_description:
            sum += i.count(',') + 1
        top_count[item] = sum
        
for i in burrito_count:
    avg_top[i] = round(top_count[i] / burrito_count[i], 2)

print("Average number of toppings per burrito are as follows:")    
for i in avg_top:
    print(i, ":", avg_top[i])

# What is the quantity ordered for each chip type?
chip_count = {}
for item in chipotle.drop_duplicates().item_name:
    if "Chip" in item:
        chip_count[item] = chipotle[chipotle.item_name==item].quantity.sum()

print("Quantity ordered for each chip type is as follow:")
for i in chip_count:
    print(i, ":", chip_count[i])

# What was the most expensive order?
chipotle.sort_values(by = 'Revenue', ascending = False).head(1)

# How many times was the Veggie Salad Bowl ordered?
sum(chipotle[chipotle['item_name']=='Veggie Salad Bowl'].value_counts())
# Alternative method => len(chipotle[chipotle['item_name']=='Veggie Salad Bowl'])

# How many times did someone order more than 1 canned soda?
len(chipotle[(chipotle.item_name=='Canned Soda') & (chipotle.quantity>1)])

# Histogram for top 5 items bought
item_count = Counter(chipotle.item_name)
df = pd.DataFrame.from_dict(item_count, orient = 'index')
df = df[0].sort_values(ascending = False)[:5]
df.plot(kind = "bar")
plt.xlabel('Item Name')
plt.ylabel('Number of items ordered')
plt.title('Most number of Chipotle items bought')
plt.show()

# Scatterplot for number of items ordered per order price
orders = chipotle.groupby('order_id').sum()
plt.scatter(x=orders.item_price, y=orders.quantity, s=50, c='blue')
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.ylim(0)