import pandas as pd
import openpyxl
# Import date class from datetime module
from datetime import date

# df = pd.read_csv(
#     'D:/statistics/kpop idols.csv')
#
#
# def underscore_rename(name):
#     return name.replace(' ', '_')
#
#
# df = df.rename(columns=underscore_rename)
#
# df1=df.groupby('Group_Group', as_index=False).\
#     aggregate({'Weight_Weight': 'sum', "Height_Height": 'count'}).\
#     sort_values('Weight_Weight', ascending=False)
#
# df2=df.Founded.value_counts()
#
# df3 = df.groupby(['Founded', 'Country']).agg({'Number_of_employees': 'mean'})

# print(df1)
# df.to_excel("C:/Users/roman/Documents/example.xlsx")
# df.to_excel("C:/Users/roman/Documents/example3.xlsx")




# Returns the current local date
today = date.today().strftime('%Y:%m:%d')
print("Today date is: ", today)

# file_name=df1

# string = 'жаба гадюка, гадюка жаба'
# print(string.split(', '))

df3 = pd.DataFrame({
    'клиент id': [1, 10, 12, 43, 100],
    'пол': [0, 1, 0, 0, 1],
    'уровень': ['medium', 'high', 'low', 'medium', 'high'],
    'возраст': [12, 43, 56, 23, 30]
})

correspondence=({
    'клиент id': 'client_id',
    'пол': 'age',
    'уровень': 'wealth',
    'возраст': 'age'
})
df3.rename(columns=correspondence, inplace=True)
# qv=df3.query('wealth=="medium" and age <30 and age>15')
df3['older_than_30'] = df3.age

print(df3)