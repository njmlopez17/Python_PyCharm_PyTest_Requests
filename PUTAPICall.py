# import:
import requests

# variable(s):
# header for GET method
headGET = {
    'Accept':'text/plain'
}

# header for PUT method
headPUT = {
    'Accept':'text/plain',
    'Content-Type': 'application/json'
}

# request data or payload
put_payload ={
    "id": 155,
    "title": "Update Title 155",
    "dueDate": "2024-10-09T16:13:25.086Z",
    "completed": True
}

# ***CODE***
print("----------------------------------------------------------------------------------------------------")

# GET response with parameters
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/12',
                        headers=headGET)


# display the response BODY with parameters
print('Before update...')
print("Successful response (with parameter) as per db content below:")
print(response.json())

# display the response CODE
print("Successful response as per code below:")
print(response.status_code)

# display the print text if expected code passed
assert response.status_code == 200
print("With status code 200, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# PUT response with parameters
responsePUT = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Activities/12',
                        headers=headPUT,
                        json=put_payload)

# display the response BODY after the update
print('After update...')
print("Successful response (after update) as per db content below:")
print(responsePUT.json())

# display the response CODE
print("Successful response as per code below:")
print(response.status_code)

# display the print text if expected code passed
assert response.status_code == 200
print("With status code 200, API test run passed.")

print("----------------------------------------------------------------------------------------------------")
