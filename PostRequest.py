#data to be sent in the post request
import json

import requests



post_data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

#send a post request to create a new post
responses = requests.post('https://jsonplaceholder.typicode.com/posts', json=post_data)

if responses.status_code == 201:
    new_post = responses.json()
    print('New post created:')
    print(json.dumps(new_post, indent=2))
else:
    print('Failed to create new post')
    print(responses.status_code)