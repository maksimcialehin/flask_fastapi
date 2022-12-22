import requests
import json
import io

from PIL import Image


response = requests.post('http://127.0.0.1:5000/')
print(response.raise_for_status)
print(json.loads(response.content.decode('utf-8')))

file = {'image': open('circus.jpg', 'rb')}
headers = {'type': 'multipart/image'}

URL = 'http://127.0.0.1:5000/'
filter = 'contour'

response = requests.post(f'{URL}/{filter}', headers=headers, files=file)
print(response.raise_for_status)

image = Image.open(io.BytesIO(response.content))
image.save('filtered.jpg', 'JPEG')
