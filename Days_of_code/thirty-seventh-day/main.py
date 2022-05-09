import requests as req
from datetime import datetime

pixel_endpoint = 'https://pixe.la/v1/users'
TOKEN = '98290sdf9034r90rfj904fj90'
USERNAME = 'junior'
GRAPH_ID = 'graph1'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# res = req.post(url=pixela_endpoint, json=user_params)
# print(res.text)


graph_endpoint = f'{pixel_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    "unit": "day",
    "type": "int",
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# res = req.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(res.text)


pixel_creation_endpoint = f'{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime(year=2022, month=6, day=9)

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('Did you code today? '),
}

# res = req.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(res.text)

update_endpoint = f'{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

new_pexel_data = {
    'quantity': '00',
}

# res = req.put(url=update_endpoint, json=new_pexel_data, headers=headers)
# print(res.text)


delete_endpoint = f'{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

res = req.delete(url=delete_endpoint, headers=headers)
print(res.text)
