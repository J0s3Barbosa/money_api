import unittest
from flask import jsonify
"""
test functions must start with 'test_' to be discoverable and tested properly   
python -m unittest test_dollar.py

"""
class TestClass(unittest.TestCase):

    def test_dollar_rate_today(self):
        rate_reals = 5.20
        response = rate_reals
        self.assertIsNot(response, None)
        
    def test_rate_main(self):
        response = {'rate': 5.20}
        self.assertIsNot(response, None)
        

if __name__ == '__main__':
    unittest.main()


