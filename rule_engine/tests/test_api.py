import unittest
import json

# tests/test_api.py
from app.api import app  # Import your Flask app

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()  # Create a test client
        self.app.testing = True

    def test_create_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        response = self.app.post('/create_rule', 
                                  json={'rule_string': rule_string})
        
        self.assertEqual(response.status_code, 200)  # Check for success
        data = json.loads(response.data)
        self.assertIn('ast', data)  # Check if AST is returned in response

    def test_combine_rules(self):
        rules = [
            "age > 30 AND department = 'Sales'",
            "age < 25 AND department = 'Marketing'"
        ]
        response = self.app.post('/combine_rules', 
                                  json={'rules': rules})
        
        self.assertEqual(response.status_code, 200)  # Check for success
        data = json.loads(response.data)
        self.assertIn('combined_ast', data)  # Check if combined AST is returned

    def test_evaluate_rule(self):
        ast = {"type": "operator", "value": "AND", "left": {"type": "condition", "value": "age > 30"}, "right": {"type": "condition", "value": "department = 'Sales'"}}  # Sample AST structure
        data = {"age": 35, "department": "Sales"}
        response = self.app.post('/evaluate_rule', 
                                  json={'ast': ast, 'data': data})
        
        self.assertEqual(response.status_code, 200)  # Check for success
        result = json.loads(response.data)
        self.assertTrue(result['result'])  # Check if evaluation result is True

if __name__ == '__main__':
    unittest.main()