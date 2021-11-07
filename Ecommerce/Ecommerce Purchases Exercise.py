# -*- coding: utf-8 -*-

"""
    Pandas Exercise
    Using Ecommerce Purchases dataset
"""

import pandas as pd
ecom = pd.read_csv('H:/ML Projects/Pandas/Ecommerce Purchases')
ecom.head()
ecom.info()

# Find the average purchase price
ecom['Purchase Price'].mean()

# Find the highest and lowest purchase prices
ecom['Purchase Price'].min()
ecom['Purchase Price'].max()

# How many people have English 'en' as their Language of choice on the website?
sum(ecom[ecom['Language']=='en'].value_counts())

# How many people have the job title of "Lawyer"?
sum(ecom[ecom['Job']=='Lawyer'].value_counts())

# How many people made the purchase during AM and PM respectively?
ecom['AM or PM'].value_counts()

# What are the 5 most common job titles?
ecom['Job'].value_counts().head(5)

# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
ecom[ecom['Lot']=='90 WT']['Purchase Price']

# What is the email of the person with the following Credit Card Number: 4926535242672853?
ecom[ecom['Credit Card']==4926535242672853]['Email']

# How many people have American Express as their Credit Card Provider *and made a purchase above $95?
sum(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].value_counts())

# How many people have a credit card that expires in 2025?
sum(ecom['CC Exp Date'].apply(lambda x: x[-2:])=='25')

# What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)?
def find_host(email):
    i = email.index('@')
    return email[i+1:]
ecom['Email'].apply(lambda x: find_host(x)).value_counts().head(5)
"""
Alternate method:
    ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)
"""