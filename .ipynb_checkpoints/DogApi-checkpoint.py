
from IPython.display import Image, display
import requests


response = requests.get('https://dog.ceo/api/breeds/image/random')

if response.status_code == 200:
    dog_data = response.json()
    image_url = dog_data.get('message', None)
    if image_url:
        print('Random Dog Image Url', image_url)
        #Display the image (works in jupyter notebook)
        display(Image(url=image_url))
    else:
        print('Image Url not found in response')
else:
    print('Failed to retrieve dog image')
    print(response.status_code)