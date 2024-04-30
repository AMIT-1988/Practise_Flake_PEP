# mocking a external api in python 
import requests 
import json 
import unittest 
from unittest.mock import patch, Mock 

# get_data() is a function that makes a request to an 
# external api and returns the data in json format 


def get_data(): #ITS A FUNCTION WHO GET DATA FROM API
	response = requests.get('https://jsonplaceholder.typicode.com/todos/1') 
	data = json.loads(response.text) 
	return data 


# TestGetData is a class that contains a test_get_data() 
# method that tests the get_data() function using the mock library 


class TestGetData(unittest.TestCase): 
	@patch('main.get_data') 
	def test_get_data(self, mock_get_data): 
		""" 
		Test that get_data() returns the correct data demonstrating the 
		use of the mock library 
		"""

		mock_data = {'userId': 1, 'id': 1, 
					'title': 'delectus aut autem', 'completed': False} 

		mock_get_data.return_value = Mock() 

		mock_get_data.return_value.json.return_value = mock_data 
		mock_get_data.return_value.status_code = 200

		result = get_data() 

		self.assertEqual(result, mock_data) 


if __name__ == '__main__': 
	unittest.main(argv=['first-arg-is-ignored'], exit=False) 
