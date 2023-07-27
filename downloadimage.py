import requests

image_url = "https://faytourimages.s3.amazonaws.com/image/Screenshot_2023-06-22_234607_20230623210329.png" 
response = requests.get(image_url)
file_path="save/image.jpg"
with open(file_path, "wb") as f:
    f.write(response.content)

with open(file_path, 'rb') as file:
    image_data = file.read()

print(image_data)
# from PIL import Image
# from io import BytesIO
# import base64

# # Load the image from file
# image_path = "save/image.jpg"
# with open(image_path, "rb") as f:
#     image_data = f.read()

# # Convert the image to base64 format
# image_base64 = base64.b64encode(image_data).decode()

# # Create a PIL Image object from the image data
# image = Image.open(BytesIO(image_data))

# # Resize the image if necessary
# # new_size = (500, 500)
# # image = image.resize(new_size)

# # Convert the PIL Image to bytes
# image_bytes = BytesIO()
# image.save(image_bytes, format=image.format)
# image_bytes = image_bytes.getvalue()

# print(image_bytes)



# Now you can include the image bytes or base64 string in your API response or request

# importing the requests library
# import io
# import requests
 
# # defining the api-endpoint
# API_ENDPOINT = "https://faytourapi-production.up.railway.app/api/Post/"
# # https://faytourapi-production.up.railway.app/api/Post/

# image_url = "https://faytourimages.s3.amazonaws.com/image/Screenshot_2023-06-22_234607_20230623210329.png"
# # Fetch the image file from the URL
# image_response = requests.get(image_url)
# image_data = image_response.content

# # Create a file-like object from the image data
# image_file = io.BytesIO(image_data)

# data = {"user":"1","body":"ayman","uploaded_images":image_bytes}
 
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjM3NDg4LCJpYXQiOjE2ODc1NTEwODgsImp0aSI6IjVhN2VjYmNkZGY3YjRiNGNiMjIyYzQ5NDdjMmFiYTVlIiwidXNlcl9pZCI6MX0.BZkCO0RW2-aAP5JH1yZtHuCN0dZhlro8tJCTmuiv-ls"
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Content-Type": "application/json"
# }
# r = requests.post(url=API_ENDPOINT, json=data,headers=headers)
# # r = requests.get(url=API_ENDPOINT,headers=headers)


 
# print(r)
# # Print the response
# post_response_json = r.json()
# print(post_response_json)