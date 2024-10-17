# import:
import requests

# variable(s):
head = {
    'Content-Type': 'application/json',
    'Authorization':'Bearer <place your own token here>' #add your token here
}

# request data or payload
request_payload ={
    "id": 7464998,
    "name": "The Hon. Aanandinii Varrier",
    "email": "varrier_aanandinii_the_hon@mohreR.test",
    "gender": "female",
    "status": "inactive"
}

# store the url in a variable
url = "https://gorest.co.in/public/v2/users"

# ***CODE***
print("----------------------------------------------------------------------------------------------------")

# POST method
postResponse = requests.post(url, headers=head, json=request_payload)

# display the response CODE
print("Successful response as per code below:")
print(postResponse.status_code)

# display the print text if expected code passed
assert postResponse.status_code == 201
print("With status code 201, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# display the json response
print("Below is the response after the POST method.")
print(postResponse.json())

print("----------------------------------------------------------------------------------------------------")

# run a GET method to validate the POST method
getResponse = requests.get(url + '/' + str(postResponse.json()['id']), headers=head)

# display the json response
print("Below is to check the data have been added after the POST method.")
print(postResponse.json())