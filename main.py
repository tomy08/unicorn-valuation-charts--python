import charts
from read_csv import read_csv
from utils import create_label_value_dict

def main():
    options = ('company', 'industry', 'country', 'continent')
    data = read_csv("data.csv")
    print('Welcome to the Unicorn companies valuation graph generator')
    print('According to which field do you want to create the graph? (Company, Industry, Country, Continent)')
    field = input()
    while field.lower() not in options:
        print('Please enter a valid option')
        field = input()
    
    field = field.lower()


    if field == 'company':
        company_data = create_label_value_dict(data, 'Company')
        charts.generate_bar_chart(list(company_data.keys()), list(company_data.values()), 'Company','Valuation (Billion dollars)','Valuation per company (companies with less than $15 billion are not shown)',threshold=15,include_others=False)

    elif field == 'industry':
        industry_data = create_label_value_dict(data, 'Industry')
        charts.generate_bar_chart(list(industry_data.keys()), list(industry_data.values()), 'Industry','Valuation (Billion dollars)', 'Companies valuation per industry',threshold=5)
    
    elif field == 'country':
        country_data = create_label_value_dict(data, 'Country')
        charts.generate_bar_chart(list(country_data.keys()), list(country_data.values()), 'Country','Valuation (Billion dollars)', 'Companies valuation per country')
    
    elif field == 'continent':
        continent_data = create_label_value_dict(data, 'Continent')
        charts.generate_bar_chart(list(continent_data.keys()), list(continent_data.values()), 'Continent','Valuation (Billion dollars)','Companies valuation per continent')
    

main()
    