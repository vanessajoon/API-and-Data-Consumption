import requests

response = requests.get('https://countriesnow.space/api/v0.1/countries')


if response.status_code == 200:
    data = response.json()
    country_list = data['data']
    total = len(country_list)
    print(f'Total Countries: {total}')
    for post in country_list:
        name = post.get('country', 'N/A')
        print(name)

else:
    print('Failed to get total number of countries')
    print(response.status_code)