import unittest
import requests
import json
import sys
sys.path.insert(0, '../configurations')
import bot_config

class TestStringMethods(unittest.TestCase):

    def test_login(self):
        headers = {"Content-type": "application/json",
        "Accept": "text/plain"}

        credentials = {"username": "root", "password":"root1234"}
        r = requests.post(bot_config.API_ENDPOINT + "authentication/login/", credentials)
        token = json.loads(r.text)["token"]
        self.assertEqual(r.status_code, 200)
        self.assertEqual(token, '62f9e4c1e669d64eedb238c3bae1a656690693f4')

    def test_create_simple_poll(self):

        headers = {"Authorization": "Token 62f9e4c1e669d64eedb238c3bae1a656690693f4"}
        voting = {"name": "Simple poll", "desc": "Question for testing", "question": "testing?", "question_opt": ["test"]}
        r = requests.post(bot_config.API_ENDPOINT + "voting/", json=voting, headers=headers)

        self.assertEqual(r.status_code, 500)

    def test_create_poll_invalid_token(self):

        headers = {"Authorization": "Token 62edb238c3bae1a656690693f4"}
        voting = {"name": "Simple poll", "desc": "Question for testing", "question": "testing?", "question_opt": ["test"]}
        r = requests.post(bot_config.API_ENDPOINT + "voting/", json=voting, headers=headers)

        self.assertEqual(r.status_code, 401)

    def test_create_multiple_poll(self):

        headers = {"Authorization": "Token 62f9e4c1e669d64eedb238c3bae1a656690693f4"}
        voting = {
                "multiple": "true",
                "name": "Multiple poll",
                "desc": "DescripcionVotacion",
                "questions": [
                {
                    "desc": "DesripcionPreguta1",
                    "options": [
                    {
                        "option": "opcion12"
                    },
                    {
                        "option": "opcion12"
                    }
                    ]
                },
                {
                    "desc": "DesripcionPreguta1",
                    "options": [
                    {
                        "option": "opcion21"
                    },
                    {
                        "option": "opcion22"
                    }
                    ]
                }
                ]
                }  
        r = requests.post(bot_config.API_ENDPOINT + "voting/", json=voting, headers=headers)

        self.assertEqual(r.status_code, 201)

    def test_vote(self):

        headers = {"Authorization": "Token 62f9e4c1e669d64eedb238c3bae1a656690693f4"}
        vote = {
                "voting": 23,
                "voter": 1,
                "vote": { "a": "3", "b": "2" }
            }
        r = requests.post(bot_config.API_ENDPOINT + "store/", json=vote, headers=headers)
        self.assertEqual(r.status_code, 401)

if __name__ == '__main__':
    unittest.main()