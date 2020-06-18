import datetime
import pandas
import collections
from pprint import pprint
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

def convert_wine_assortment_excel_to_dict():
    excel_wine_assortment = pandas.read_excel('wine2.xlsx', sheet_name='Лист1', keep_default_na=False)
    wine_dict = excel_wine_assortment.to_dict(orient='record')
    return wine_dict

def sort_wine_by_category(wine_dict):
    sorted_wine_by_category = collections.defaultdict(list)
    for number, __ in enumerate(wine_dict):
        category = wine_dict[number]['Категория']
        sorted_wine_by_category[category]
        sorted_wine_by_category[category].append(wine_dict[number])
    return sorted_wine_by_category

def count_company_age():
    now = datetime.datetime.now()
    event1 = datetime.datetime(year=1920, month=1, day=1)
    event2 = datetime.datetime(year=now.year, month=now.month, day=now.day)
    delta = event2 - event1
    age_amount = delta.days // 365
    return age_amount

def main():
    actual_company_age = count_company_age()
    wine_dict = convert_wine_assortment_excel_to_dict()
    sorted_wine_dict = sort_wine_by_category(wine_dict)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        years_amount=actual_company_age,
        sorted_wine_dict=sorted_wine_dict
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
