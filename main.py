import charts
from read_csv import read_csv
import re

def main():
    options = ('company', 'industry', 'country', 'continent')
    data = read_csv("data.csv")
    print('According to which field do you want to create the graph? (Company, Industry, Country, Continent)')
    field = input()
    while field.lower() not in options:
        print('Please enter a valid option')
        field = input()
    
    field = field.lower()
    if field == 'company':
        charts.create_pie_chart(data, 'Company')
    elif field == 'industry':
        industry_data = {}
        for item in data:
            valuation = re.sub(r'%|B|\$', '', item['Valuation'])
            valuation_number = int(valuation)
            if (item['Industry'] not in industry_data):
                industry_data.update({item['Industry']: valuation_number})
            else:
                industry_data[item['Industry']] += valuation_number
        charts.generate_pie_chart(list(industry_data.keys()), list(industry_data.values()), 'Valuation per industry')
    elif field == 'country':
        charts.create_pie_chart(data, 'Country')
    elif field == 'continent':
        charts.create_pie_chart(data, 'Continent')
    

main()
    