import requests

base_url = 'https://localhost:8080'

response1 = requests.get(f'{base_url}/cars').json()
response2 = requests.get(f'{base_url}/manufacturers').json()
response3 = requests.get(f'{base_url}/cars/prices').json()

print(response3)

