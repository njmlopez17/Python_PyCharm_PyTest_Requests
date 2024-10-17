# import:
import requests
import json

# variable(s):

# store the url in a variable
url = "https://reqres.in/"

# header(s)
head = {
    'Content-Type': 'application/json'
}

# request data or payload from a JSON file
json_file = open('./sample_users.json')
json_load = json.load(json_file)

# request data or payload
# request_payload ={
#     "name": "Test",
#     "job": "QA"
# }

# ***CODE***
print("----------------------------------------------------------------------------------------------------")

# POST method
response = (requests.post(
    url=url+"api/users",
    headers=head,
    data=json.dumps(json_load) # --this is for passing from other files (including json file)
    # json=json_load --this is the cmd if only passing from a json file
))

# display the response CODE
print("Successful response as per code below:")
print(response.status_code)

# display the print text if expected code passed
assert response.status_code == 201
print("With status code 201, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# display the json response
print("Below is the response after the POST method (JSON file display.")
print(response.json())
print("Below is the response after the POST method (TEXT file display.")
print(response.text)
