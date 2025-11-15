## Program to check if the file is json or not and extract details on the json file
import json
with open("/home/samir/Desktop/python/hello.json",'r') as file:
    data=json.load(file)

if not isinstance(data,dict):
    print('Data is not in json formt')
    exit(1)

name=data['name']
age=data['age']
email=data['email']
order_id=data['orders'][0]['orderId']
print(order_id)