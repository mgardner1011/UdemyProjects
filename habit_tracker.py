import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
username = 'username'
token = 'api token'
graph_id = 'graph1'


# create user
user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# create a habit tracking graph
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_config = {
    'id': graph_id,
    'name': 'Coding Graph',
    'unit': 'hr',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# add entry/pixel to habit tracking graph
today = datetime.now()

pixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many hours did you practice coding today?'),
}
pixel_creation_endpoint = f'{graph_endpoint}/{graph_id}'


response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

# update entry/pixel in habit tracking graph

update_params = {
    'quantity': '5.7'
}
pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

response = requests.put(url=pixel_update_endpoint, json=update_params, headers=headers)
print(response.text)

# delete pixel/entry from habit tracking graph

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)
