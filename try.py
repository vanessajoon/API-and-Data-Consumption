import requests

response = requests.get('https://restcountries.com/v3.1/region/africa')

if response.status_code == 200:
    data = response.json()
    print('displaying 5 first country names from the region africa')
    for post in data[:5]:
        name = post.get('name', {}).get('common', 'N/A')
        print(name)
else:
    print('Failed retrieving first 5 african countries')
    print(response.status_code)