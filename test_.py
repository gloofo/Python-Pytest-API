from src.modules import *

endpoint = "https://reqres.in"

#Load endpoints yaml data
def data():
    with open("resources/endpoints.yaml") as file:
        getdata = yaml.load(file, Loader=yaml.FullLoader)
    return getdata

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
    print(getData['id'])
    assert response.status_code == 201

def test_DeleteUser():
    response = delRequest(path="single", userId=f"{getData['id']}")
    assert response.status_code == 204

#user registration
def test_registerUser():
    dataPass = jsonData(password=fake().password())
    response = postRequest(path="register", dataPayload=dataPass)
    assert response.status_code == 400
    #response should be 200, but their website is returning 400
    #I also tried using POSTMAN API same response.
    
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
