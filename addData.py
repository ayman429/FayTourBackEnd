import requests

# image_url = "https://faytourimages.s3.amazonaws.com/image/Screenshot_2023-06-22_234607_20230623210329.png" 
# response = requests.get(image_url)
# file_path="save/image.jpg"
# with open(file_path, "wb") as f:
#     f.write(response.content)

# with open(file_path, 'rb') as file:
#     image_data = file.read()

# print(image_data)
from list import data
baseUrl = "https://faytourimages.s3.amazonaws.com/"
id=data[0]['id']
print(id)
list1=[]
listoflist=[]

for i in range(len(data)):
    
    # if data[i]['id'] == id:
        list1.append(baseUrl+data[i]["originalImage"])
print(list1)
print(len(list1))

    # else:
    #     # print(list1)
    #     id=data[i]['id']
    #     listoflist.append(list1)
    #     # print(id)
    #     list1=[]
# listoflist.append(list1) 
# print(len(listoflist))
# print(listoflist)
listoflist = list1
# with open("save/"+"hotelImages.txt", "a") as contentFile:
#         contentFile.write(str(listoflist))

for i in range(len(listoflist)):
    # for j in range(len(listoflist[i])):
        response = requests.get(listoflist[i])
        image = listoflist[i].replace("https://faytourimages.s3.amazonaws.com/image/","")
        file_path="save/h"+str(i+1)+"/"+image
        with open(file_path, "wb") as f:
            f.write(response.content)

        with open(file_path, 'rb') as file:
            image_data = file.read()


# from hotelData import hotel
# print(hotel[0])


