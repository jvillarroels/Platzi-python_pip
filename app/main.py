# Nro 3
# -----------------------------------------------------------
import utils
import read_csv
import charts
import pandas as pd

# 12:27

def run():
    '''    
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item : item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    '''

    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'South America']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

    data = read_csv.read_csv('data.csv')
    country = input('Type Country ==> ')
    print(country)
    
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
    run()

# ---

'''
# Nro 2
# -----------------------------------------------------------
import utils
import read_csv
import charts
# 12:27

def run():
    data = read_csv.read_csv('./app/data.csv')
    country = input('Type Country ==> ')
    
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()
'''
# ---

'''
# Nro 1
# -----------------------------------------------------------

import utils

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)
    
    country = input('Type Country => ')
    
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()
'''