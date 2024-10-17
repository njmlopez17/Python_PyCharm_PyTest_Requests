# import:
import requests

# variable(s):
head = {
    'Accept':'text/plain',
    'Content-Type': 'application/json'
}

# request data or payload
request_payload ={
    "id": 32,
    "title": "Activity Testing 03",
    "dueDate": "2024-10-09T16:13:25.086Z",
    "completed": True
}

# ***CODE***
print("----------------------------------------------------------------------------------------------------")

# POST method
response = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Activities',
                         headers=head,
                         json=request_payload)

# display the response CODE
print("Successful response as per code below:")
print(response.status_code)

# display the print text if expected code passed
assert response.status_code == 200
print("With status code 200, API test run passed.")

print("----------------------------------------------------------------------------------------------------")

# display the json response
print("Below is the response after the POST method.")
print(response.json())

print("----------------------------------------------------------------------------------------------------")

#sample test validation of ensuring what was sent in the request is what comes back as expected from the response
data = response.json()
assert (data ['id']) == 32
