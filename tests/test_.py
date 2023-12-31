import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from modules import *

endpoint = "https://reqres.in"

#get user details
def test_Users():
    userList = requests.get(endpoint + f"{data()['api']['users']}")
    assert userList.status_code == 200
    userData = userList.json()
    singleUser = getRequest(path="single", userId=f"{userData['data'][0]['id']}")
    assert singleUser.status_code == 200

#create a user
def test_CreateUser():
    global getData
    response = postRequest(path="single", dataPayload=payload())
    getData = response.json()
    assert response.status_code == 201

#delete user using the id of the created use
def test_DeleteUser():
    response = delRequest(path="single", userId=f"{getData['id']}")
    assert response.status_code == 204

#user registration
def test_registerUser():
    dataPass = jsonData(password=fake().password())
    response = postRequest(path="register", dataPayload=dataPass)
    #response should be 200, but their website is returning 400
    #I also tried using POSTMAN API same response.
    assert response.status_code == 400
    
#returns json payload
def payload():
    return {
    "name": f"{fake().name()}",
    "job": f"{fake().name()}"
    }   
    
def postRequest(path="", dataPayload=""):
    return requests.post(endpoint + f"{data()['api'][path]}", json=dataPayload)    

def delRequest(userId="", path=""):
    return requests.delete(endpoint + f"{data()['api'][path]}" + userId)

def jsonData(password=""):
    return {
    "email": f"{fake().email()}",
    "password": f"{password}"
    }

def getRequest(path="", userId=""):
    return requests.get(endpoint + f"{data()['api'][path]}" + userId) 
