

import json
import unittest
import requests

BASE_URL = 'http://localhost:5000'


class TestApi(unittest.TestCase):
    def setUp(self):
        print('Init Tests')
        self.login = {
            "nombres": "test",
            "apellidos": "api",
            "correo": "test@gmail.com",
            "contrasena": "123456"
        }

    def test_create_user(self):
        body = self.login
        response = requests.post(
            BASE_URL+"/register/registrar", json=body)
        data = response.json()

        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['status'], 201)
        self.assertEqual(response.status_code, 201)

    def test_login_user_not_found(self):
        body = {"correo": "falso@gmail.com",
                "contrasena": "falso"}

        response = requests.post(
            BASE_URL+"/login", json=body)

        data = response.json()

        self.assertEqual(data['message'], 'user not found')
        self.assertEqual(data['status'], 404)
        self.assertEqual(response.status_code, 404)

    def test_login_valid_user(self):
        body = {"correo": self.login["correo"],
                "contrasena": self.login["contrasena"]}
        response = requests.post(
            BASE_URL+"/login", json=body)

        data = response.json()

        self.assertEqual(data['message'], 'success')
        self.assertEqual(
            data['data'], {"name": self.login['nombres'], "email": self.login["correo"]})
        self.assertEqual(data['status'], 200)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
