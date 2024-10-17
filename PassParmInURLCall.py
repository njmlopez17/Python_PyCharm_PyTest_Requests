# import:
import requests

# variable(s):

# store the url in a variable
url = "https://gorest.co.in/public/v2/users"

# parameters to be passed and part of the request
parm = {
    'page': 1,
    'per_page': 2
}

# ***CODE***
print("----------------------------------------------------------------------------------------------------")

# GET method
getResponse = requests.get(url, params=parm)

# display the response CODE
print("Successful response as per code below:")
print(getResponse.status_code)

# display the print text if expected code passed
assert getResponse.status_code == 200
print("With status code 200, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# display the json response
print("Below is the response after the POST method.")
print(getResponse.json())