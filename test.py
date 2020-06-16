import collections
import pandas
from pprint import pprint

def sort_wine_by_category(wine_dict):
    sorted_wine_by_category = collections.defaultdict(list)
    for number, __ in enumerate(wine_dict):
        category = wine_dict[number]['Категория']
        sorted_wine_by_category[category]
        sorted_wine_by_category[category].append(wine_dict[number])
    return sorted_wine_by_category

excel_wine_assortment = pandas.read_excel('wine2.xlsx', sheet_name='Лист1')
wine_dict = excel_wine_assortment.to_dict(orient='record')

pprint(sort_wine_by_category(wine_dict))





#wines_by_category = {}
#for num, __ in enumerate(wine_dict):
#   category = wine_dict[num]['Категория']
#   if category not in wines_by_category.keys():
#        wines_by_category[category] = []
#        wines_by_category[category].append(wine_dict[num])
#
#print(wines_by_category)





#white_wines = []
#red_wines = []
#other_drinks = []
#
#sorted_wine_dict = {
#    'Белые вина': white_wines,
#    'Красные вина': red_wines,
#    'Напитки': other_drinks
#}
#
#for num, __ in enumerate(wine_dict):
#    category = wine_dict[num]['Категория']
#    if category == 'Белые вина':
#        white_wines.append(wine_dict[num])
#    elif category == 'Красные вина':
#        red_wines.append(wine_dict[num])
#    else:
#        other_drinks.append(wine_dict[num])
#
#pprint(sorted_wine_dict)