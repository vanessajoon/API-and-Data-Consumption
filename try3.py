import json

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
# data = response.json()
# print(json.dumps(data, indent=4))

if response.status_code == 200:
    data = response.json()
    for post in data[:5]:
        name = post.get('name', 'N/A')
        email = post.get('email', 'N/A')
        phone = post.get('phone', 'N/A')
        address = post.get('address', {}).get('city', 'N/A')



        print(f'Fullname: {name}')
        print(f'Email: {email}')
        print(f'Phone Number: {phone}')
        print(f'City: {address}')
        print('*' * 30)
else:
    print('Failed to get users details')
    print(response.status_code)