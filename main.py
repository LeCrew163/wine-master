import datetime
import pandas
from pprint import pprint
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

def convert_wine_assortment_excel_to_dict():
    excel_wine_assortment = pandas.read_excel('wine.xlsx', sheet_name='Лист1')
    wine_dict = excel_wine_assortment.to_dict(orient='record')
    return wine_dict

def count_company_age():
    now = datetime.datetime.now()
    event1 = datetime.datetime(year=1920, month=1, day=1)
    event2 = datetime.datetime(year=now.year, month=now.month, day=now.day)
    delta = event2 - event1
    age_amount = delta.days // 365
    return age_amount

def main():
    actual_company_age = count_company_age()
    wines = convert_wine_assortment_excel_to_dict()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        years_amount=actual_company_age,
        wines=wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
