import requests
import json


countries_to_get = ["france", "nigeria", "japan", "canada"]
for country_name in countries_to_get:
    url = f'https://restcountries.com/v3.1/name/{country_name}'
    response = requests.get(url)

    if response.status_code == 200:
        countries = response.json()
        for country in countries:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]
            region = country.get('region', 'N/A')
            population = country.get('population', 'N/A')
            print(f'Country: {name}')
            print(f'Capital: {capital}')
            print(f'Region: {region}')
            print(f'Population: {population}')
            print('-' * 30)

    else:
        print('Failed to retrieve country data')
        print(response.status_code)

