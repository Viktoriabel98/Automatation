import requests
from data import *


class CompanyApi:

    def __init__(self, url):
        self.url = url

    def get_token(self, authorization):
        resp = requests.post(self.url + '/auth/login', json=authorization)
        return resp.json()["userToken"]

    def create_company(self, name, description):
        company = {
            'name': name,
            'description': description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token(authorization)
        resp = requests.post(
            self.url + '/company', json=company, headers=my_headers)
        return resp.json()['id']