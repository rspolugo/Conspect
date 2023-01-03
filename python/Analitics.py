import pandas as pd
import openpyxl
# Import date class from datetime module
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_csv(
#     'D:/statistics/kpop idols.csv')
# #
# #
# def underscore_rename(name):
#     return name.replace(' ', '_')
# #
# #
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

# today = date.today().strftime('%Y:%m:%d')
# print("Today date is: ", today)

# file_name=df1

#### separation with symbol

# string = 'frog viper, viper frog'
# print(string.split(', '))

#### creating df

# df3 = pd.DataFrame({
#     'клиент id': [1, 10, 12, 43, 100],
#     'пол': [0, 1, 0, 0, 1],
#     'уровень': ['medium', 'high', 'low', 'medium', 'high'],
#     'возраст': [12, 43, 56, 23, 30]
# })
#
# #### rename of columns
#
# correspondence=({
#     'клиент id': 'client_id',
#     'пол': 'sex',
#     'уровень': 'wealth',
#     'возраст': 'age'
# })
# df3.rename(columns=correspondence, inplace=True)
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

#### aggregating function from file

# df6=pd.read_csv('https://stepik.org/media/attachments/lesson/359209/companies.csv', sep=';')
# print(df6.groupby('company').agg({'income': 'mean'}))
# df6.to_excel('D:/statistics/example_stepik.xlsx')

# def read_path_and_agg_and_print(path):
#     df6=pd.read_csv(path, sep=';')
#     res=print(df6.groupby('company').agg({'income': 'mean'}))
#     return res
# read_path_and_agg_and_print('https://stepik.org/media/attachments/lesson/359209/companies.csv')

#### the most popular platform

# taxi = pd.read_csv('https://stepik.org/media/attachments/lesson/359240/taxi_peru.csv', sep=';', parse_dates=['start_at', 'end_at', 'arrived_at'])
# print(taxi.dtypes)

# print(taxi.shape) #count of strings
# print(taxi.source.value_counts()/taxi.shape[0])
# or the same
# print(taxi.source.value_counts(normalize=True)) #share part
# print(
#     taxi
#       .source
#       .value_counts(normalize=True)
#       .mul(100)
#       .round(2)
# ) #percent |.idxmax - largest value | .mul(100) - the same like *100

#### distribution driver points

# driver_score_counts=taxi\
#     .driver_score\
#     .value_counts(normalize=True)\
#     .mul(100)\
#     .round(2)\
#     .reset_index()\
#     .rename(columns={'index': 'driver_score', 'driver_score': 'percentage'})\
#     .sort_values('driver_score', ascending=False)
#
# print(driver_score_counts)
#
# #### chart analisys
#
# ax=sns.barplot(x='driver_score', y='percentage', data=driver_score_counts, color='blue', alpha=0.5)
#
# ax.set(xlabel='Driver score', ylabel='Percentage')
# sns.despine() #put away part of graph's frame
# plt.show()

#### apply method

# df1 = pd.read_csv(
#     'D:/statistics/kpop idols.csv')
# def underscore_rename(name):
#     return name.replace(' ', '_')
#
# def split_method_for_column(name):
#     return name.split(' ')[-1]
#
# df = df1.rename(columns=underscore_rename)
#
# df = df.astype(str)

#5df['surname'] = df.Full_Name_Full_Name.apply(split_method_for_column)
#or the same
#### lamda
# df['surname'] = df.Full_Name_Full_Name.apply(lambda x: x.split(' ')[-1])

#### project

#1 Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;.
# Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные.

# bookings = pd.read_csv('D:/statistics/code/2/Задания/Минипроект/bookings.csv', sep=';')
# bookings_head=bookings.head(7)
#2 Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.

# def space_to_underscore(name):
#     return name.replace(' ', '_').lower()
#
# bookings=bookings.rename(columns=space_to_underscore)
#3 Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.

# print(bookings.\
#       query('is_canceled==0')\
#       .country\
#       .value_counts()[:5]
#       )
#4 На сколько ночей в среднем бронируют отели разных типов?

# print(bookings.columns)

# print(bookings\
#       .groupby('hotel',as_index=False)\
#       .agg({'stays_total_nights': 'mean'})\
#       .round(2))

#5 Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type).
# Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?

# print(bookings\
#     .query('assigned_room_type!=reserved_room_type')\
#     .shape[0])

#6 Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов

# print(bookings.\
#     query('arrival_date_year == 2016')\
#     .arrival_date_month\
#     .value_counts())
#
# print(bookings.\
#     query('arrival_date_year == 2017')\
#     .arrival_date_month\
#     .value_counts())
# print(bookings.query('hotel == "City Hotel" and is_canceled == 1')
#       .groupby('arrival_date_year')
#       .arrival_date_month
#       .value_counts())

####7 describe (or mean()) Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?
# print(bookings
#       [['adults', 'children', 'babies']].mean()
#       )

#8 Создайте колонку total_kids, объединив children и babies. Отели какого типа в среднем пользуются большей популярностью у клиентов с детьми?
# bookings['total_kids'] = bookings.children + bookings.babies
#
# print(bookings.
#       groupby('hotel').
#       agg({'total_kids': 'mean'}).
#       round(decimals=2).
#       max())
#9
# bookings['has_kids']=bookings.total_kids>0
#
# no_kids_churn=bookings.query('is_canceled==1 and has_kids==False').shape[0]/bookings.query('has_kids==False').shape[0]
# print(round(no_kids_churn*100,2))
# yes_kids_churn=bookings.query('is_canceled==1 and has_kids==True').shape[0]/bookings.query('has_kids==True').shape[0]
# print(round(yes_kids_churn*100,2))

#### project2
#1 Импортируйте библиотеку pandas как pd. Загрузите два датасета user_data и logs.
# Проверьте размер таблицы, типы переменных, наличие пропущенных значений, описательную статистику.
user_data = pd.read_csv('D:/statistics/code/3/Задания/Минипроект/user_data.csv', sep=',')
logs = pd.read_csv('D:/statistics/code/3/Задания/Минипроект/logs.csv', sep=',')
print(user_data)
# print(user_data.shape)
# print(user_data.dtypes)
# print(user_data.isna().sum()) #or the same isnull()

print(logs)
# print(logs.shape)
# print(logs.dtypes)
# print(logs.isna().sum())

# print(logs.columns)
# print(user_data.columns)
#
# print(logs.platform.nunique())
#
# print(user_data.describe())# описательная статистика
# print(logs.describe())

#2 Какой клиент совершил больше всего успешных операций? (success == True)

# success_number=logs.\
#        query('success == True')\
#       .groupby('client')\
#       .agg({'platform': 'count'})\
#       .rename(columns={'platform': 'success_number'})\
#       .sort_values('success_number', ascending=False)
#
# print(success_number)

#3 С какой платформы осуществляется наибольшее количество успешных операций?

# print(logs.query('success == True').platform.value_counts().idxmax())

#4 Какую платформу предпочитают премиумные клиенты?

# udata_premium = user_data.query('premium==True')
# merge=udata_premium.merge(logs, how='left', on='client')
# print(merge.groupby("platform").
#       agg({'age': 'count'}).
#       sort_values('age', ascending=False)) #or value_counts()

#5 Визуализируйте распределение возраста клиентов в зависимости от типа клиента (премиум или нет)

barplot_clients=user_data.sort_values('premium')
# ax=sns.distplot(barplot_clients.query('premium==False').age)
# ax1=sns.distplot(barplot_clients.query('premium==True').age)
# #
# ax.set(xlabel='age', ylabel='premium')
# sns.despine() #put away part of graph's frame
# plt.show()
# or on two different diagrams
# fig, ax = plt.subplots(nrows=2, ncols=1)
# sns.distplot(barplot_clients.query('premium==True').age, ax=ax[0], color='green')
# sns.distplot(barplot_clients.query('premium==False').age, ax=ax[1], color='red')
# plt.show()

#6 Постройте график распределения числа успешных операций

success_trans = logs.groupby('client').agg({'success': 'sum'})
sns.distplot(success_trans, kde=False)
plt.show()

print(success_trans)
print(success_trans.success.value_counts())