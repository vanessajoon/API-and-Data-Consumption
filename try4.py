import json
from csv import excel_tab

import requests

try:
    number = int(input('Enter a number from 1-10 '))
    if number not in range(1, 11):
        print('Enter number only from 1-10')
        exit()
except ValueError:
    print('Please enter a number and not digits')

try:
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={number}')
    # data = response.json()
    # print(json.dumps(data, indent=4))

    if response.status_code == 200:
        data = response.json()
        if data:
            for posts in data:
                title = posts.get('title', 'N/A')
                print(f'Title: {title}')
                print('*' * 40)
        else:
            print('No posts found for this user data')
    else:
        print('Failed to retrieve user')
        print(response.status_code)
except requests.exceptions.ConnectionError:
    print('Network problem, please check your connection')
except requests.exceptions.Timeout:
    print('The request timed out. Try again later')
except requests.exceptions.HTTPError as err:
    print(f'Http error occurred: {err}')
except Exception as err:
    print(f'Something went wrong: {err}')
