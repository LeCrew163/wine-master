import collections
import pandas
from pprint import pprint

wine = pandas.read_excel('wine2.xlsx', sheet_name='Лист1')
wine_dict = wine.to_dict(orient='record')


sorted_wine_dict = collections.defaultdict(list)
sorted_wine_dict['Белые вина']
sorted_wine_dict['Красные вина']
sorted_wine_dict['Напитки']

for num, wine_infos in enumerate(wine_dict):
    sorted_wine_dict['Белые вина'].append(wine_infos)

pprint(sorted_wine_dict)


#white_wines = []
#red_wines = []
#other_drinks = []
#
#sorted_wine_dict = {
#    'Белые вина': white_wines,
#    'Красные вина': red_wines ,
#    'Напитки': other_drinks
#}
#
#for num, __ in enumerate(wine_dict):
#    if wine_dict[num]['Категория'] == 'Белые вина':
#        white_wines.append(wine_dict[num])
#    elif wine_dict[num]['Категория'] == 'Красные вина':
#        red_wines.append(wine_dict[num])
#    else:
#        other_drinks.append(wine_dict[num])
#
#pprint(sorted_wine_dict)


