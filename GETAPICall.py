# import:
import requests

# variable(s):
head = {
    'Accept':'text/plain'
}

# ***CODE***
print("----------------------------------------------------------------------------------------------------")

# GET response without parameters
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities')

# display the response BODY
print("Successful response (without parameter) as per db content below:")
print(response.json())

# display the response CODE
print("Successful response as per code below:")
print(response.status_code)

# expected response CODE
assert response.status_code == 200
print("With status code 200, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# GET response with parameters
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/2')

# display the response BODY with parameters
print("Successful response (with parameter) as per db content below:")
print(response.json())

# display the response CODE
print("Successful response as per code below:")
print(response.status_code)

# display the print text if expected code passed
assert response.status_code == 200
print("With status code 200, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# GET response with header validation
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/2',
                        headers=head)

# display the response CODE
print("Successful response (no error on header) as per code below:")
print(response.status_code)

# expected response CODE
assert response.status_code == 200
print("With status code 200, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# expected response CODE is 200 but with error
# assert response.status_code == 201
