import requests
import json
from IPython.display import Image, display

#Example Get Request with JSONPlaceholder
#in this example we will retrieve a list of posts from JSONPlaceholder using a get method

#Sned a GET request to the JSONPlaceholder posts endpoint
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response) check the status

#Check if the request was successful
if response.status_code == 200:
    posts = response.json()
   # print(posts) check whether it came in a json format
    print('Displaying the first 3 posts')
    for post in posts[:3]:
        print(post)
else:
    print('Failed to retrieve posts')
    print(response.status_code)