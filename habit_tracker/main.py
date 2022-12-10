import requests
from datetime import datetime

TOKEN = 'ghasl5hasne8wn2o'
USERNAME = 'bucketgetter'
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    'token': TOKEN, # basically api key that I generate myself
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# create the user (after created, we dont need it anymore)
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

# create the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

# put the token in a http header, this is how we authenticate ourselves
headers = {
    'X-USER-TOKEN': TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

# to look at graph: https://pixe.la/v1/users/bucketgetter/graphs/graph1.html

# Post a pixel
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
date_in_the_past = datetime(year=2022, month=11, day=7)
today = datetime.now()
print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"

}
#response = requests.post(url=pixel_post_endpoint, json=pixel_data, headers=headers)
#print(response.text)


# Update a pixel, with put request
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {"quantity": '3'}
#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

# Delete a pixel, with delete request
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)








