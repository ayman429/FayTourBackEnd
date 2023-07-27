
# importing the requests library
import io
import requests
 
# defining the api-endpoint
API_ENDPOINT = "https://faytourapi-production.up.railway.app/api/Post/"
# https://faytourapi-production.up.railway.app/api/Post/

image_url = "https://faytourimages.s3.amazonaws.com/image/Screenshot_2023-06-22_234607_20230623210329.png"
# Fetch the image file from the URL
image_response = requests.get(image_url)
image_data = image_response.content


data = {"user":"1","body":"ayman"}
files = {'image': open('save/h1/163854883.jpg', 'rb')}
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjM3NDg4LCJpYXQiOjE2ODc1NTEwODgsImp0aSI6IjVhN2VjYmNkZGY3YjRiNGNiMjIyYzQ5NDdjMmFiYTVlIiwidXNlcl9pZCI6MX0.BZkCO0RW2-aAP5JH1yZtHuCN0dZhlro8tJCTmuiv-ls"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
r = requests.post(url=API_ENDPOINT, json=data, files=files,headers=headers)
# response = requests.request("POST", API_ENDPOINT, files=files, headers=headers)
# r = requests.get(url=API_ENDPOINT,headers=headers)
# print(response.text)
# Print the response
# print(r)
post_response_json = r.json()
print(post_response_json)