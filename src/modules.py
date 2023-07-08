import pytest
import requests
import yaml
from faker import Faker

def fake():
    fake = Faker()
    return fake

#Load endpoints yaml data
def data():
    with open("resources/endpoints.yaml") as file:
        getdata = yaml.load(file, Loader=yaml.FullLoader)
    return getdata