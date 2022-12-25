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




#### Returns the current local date
today = date.today().strftime('%Y:%m:%d')
print("Today date is: ", today)

# file_name=df1

#### separation with symbol
# string = 'жаба гадюка, гадюка жаба'
# print(string.split(', '))

#### creating df
df3 = pd.DataFrame({
    'клиент id': [1, 10, 12, 43, 100],
    'пол': [0, 1, 0, 0, 1],
    'уровень': ['medium', 'high', 'low', 'medium', 'high'],
    'возраст': [12, 43, 56, 23, 30]
})

#### rename of columns
correspondence=({
    'клиент id': 'client_id',
    'пол': 'sex',
    'уровень': 'wealth',
    'возраст': 'age'
})
df3.rename(columns=correspondence, inplace=True)
# qv=df3.query('wealth=="medium" and age <30 and age>15') #creating of query

#### creating columns a
# df3['older_than_30'] = df3.age>30

#### counting of unique values
# print(df3.nunique())
# print(df3)

#### merger of two dfs
# df4=pd.DataFrame({
#     'client_id':[10, 12, 7250, 8619, 43],
#     'amount':[42331, 88420, 1714, 80572, 57549],
#     'date':[1585425830, 1585429536, 15854427761, 1585427077, 1585426290]
# })
# merge=df4.merge(df3, how='left', on='client_id')
# print(merge)

# df6=pd.read_csv('https://stepik.org/media/attachments/lesson/359209/companies.csv', sep=';')
#
# print(df6.groupby('company').agg({'income': 'mean'}))
# df6.to_excel('D:/statistics/example_stepik.xlsx')

#### aggregating function from file
def read_path_and_agg_and_print(path):
    df6=pd.read_csv(path, sep=';')
    res=print(df6.groupby('company').agg({'income': 'mean'}))
    return res
read_path_and_agg_and_print('https://stepik.org/media/attachments/lesson/359209/companies.csv')