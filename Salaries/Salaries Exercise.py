# -*- coding: utf-8 -*-

"""
    Pandas Exercise
    Using Salaries dataset
"""

import pandas as pd
sal = pd.read_csv('H:/ML Projects/Pandas/Salaries.csv')
sal.head()
sal.info()

# Finding average BasePay
sal['BasePay'].mean()

# Finding highest amount of OvertimePay
sal['OvertimePay'].max()

# What is the job title of JOSEPH DRISCOLL?
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']

# How much does JOSEPH DRISCOLL make (including benefits)?
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

# What is the name of the highest paid person (including benefits)?
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName']

# Is there something strange about the lowest paid person (including benefits)?
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]
# Pay is negative!

# What was the average BasePay of all employees per year?
sal.groupby('Year').mean()['BasePay']

# How many unique job titles are there?
sal['JobTitle'].nunique()

# What are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)

# How many job titles were represented by only one person in 2013?
sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)

# How many people have the word Chief in their job title?
def chief(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
sum(sal['JobTitle'].apply(lambda x: chief(x)))

# Is there a correlation between length of the job title string and salary?
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len', 'TotalPayBenefits']].corr()
# No correlation