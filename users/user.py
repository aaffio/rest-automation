from pyunitreport import HTMLTestRunner
import requests
import unittest


class User(unittest.TestCase):

    def test_get_user_by_id(self):
        customer_id = 1
        print('getting user by id : ' + str(customer_id))
        # suppose customer id is added in url
        url = "https://run.mocky.io/v3/233c2093-e1c0-4bad-85ad-73b19322e593?customer_id" + str(customer_id)
        response = requests.get(url)
        if response.status_code == 200:

            self.print_response(response)

    def print_response(self, response):
        print(response.json())
        # get json by it's attribute
        print(response.json()['id'])

    def test_get_users(self):
        print('getting list of users')
        url = "https://run.mocky.io/v3/4bec55e4-a566-4422-abfc-3c5aecd85064"
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='user-test'))
