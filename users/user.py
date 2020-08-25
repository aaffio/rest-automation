import HtmlTestRunner
import requests
import unittest
import logging

logging.basicConfig(filename="users.log", level=logging.DEBUG)


class User(unittest.TestCase):

    def test_get_user_by_id(self):
        """test_get_user_by_id"""
        customer_id = 1
        print('getting user by id : ' + str(customer_id))
        # suppose customer id is added in url
        url = "https://run.mocky.io/v3/233c2093-e1c0-4bad-85ad-73b19322e593?customer_id" + str(customer_id)
        response = requests.get(url)
        assert 200 == response.status_code
        if response.status_code == 200:
            self.print_response(response)

    @staticmethod
    def print_response(response):
        print(response.json())
        logging.info(response.json())
        # get json by it's attribute
        print(response.json()['id'])
        logging.debug(response.json()['id'])

    @staticmethod
    def test_get_users():
        """test_get_users"""
        print('getting list of users')
        url = "https://run.mocky.io/v3/4bec55e4-a566-4422-abfc-3c5aecd85064"
        response = requests.get(url)
        assert 200 == response.status_code
        if response.status_code == 200:
            print(response.json())
            print(response.content())
            logging.info(response.json())


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
