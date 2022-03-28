import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_API_KEY = "secret12345"
Username = "connorske"
Graph = "graph1"

#Tracker Website to view #'https://pixe.la/v1/users/connorske/graphs/graph1.html'
today = datetime.now()
#other_date = datetime(year=2020, month=7, day=23)

user_params = {
    'token': PIXELA_API_KEY,
    'username': Username,
    'agreeTermsOfService': "yes",
    'notMinor': "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#
# graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Miles",
#     "type": "float",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN":PIXELA_API_KEY
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#post request
add_date = datetime(year=2022, month=3, day=27).strftime("%Y%m%d")

value_endpoint = f"{pixela_endpoint}/{Username}/graphs/{Graph}"
value_data = {
    "date":today.strftime("%Y%m%d"),
    # "date": add_date,
    "quantity":input("How many miles did you cycle today? ")
}

response = requests.post(url=value_endpoint, json=value_data, headers=headers)
print(response.text)

#PUT#
# Updatedate = datetime(year=2022, month=3, day=27).strftime("%Y%m%d")
# update_endpoint = f"{pixela_endpoint}/{Username}/graphs/{Graph}/{Updatedate}"
#
# update_data ={
#     "quantity":"9.5"
# }

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)


# #Delete#
# delete_date = datetime(year=2022, month=3, day=28).strftime("%Y%m%d")
# delete_endpoint = f"{pixela_endpoint}/{Username}/graphs/{Graph}/{delete_date}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
