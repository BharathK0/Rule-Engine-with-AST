import unittest
from app.rules import create_rule, combine_rules, evaluate_rule
from app.ast import Node

# tests/test_rules.py

class TestRules(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        
        self.assertIsInstance(ast, Node)  # Check if it's a Node
        self.assertEqual(ast.type, "operator")  # Check if root is an operator
        self.assertEqual(ast.value, None)  # Check if value is None for operator

    def test_combine_rules(self):
        rules = [
            "age > 30 AND department = 'Sales'",
            "age < 25 AND department = 'Marketing'"
        ]
        combined_ast = combine_rules(rules)
        
        self.assertIsInstance(combined_ast, Node)  # Check if combined AST is a Node
        self.assertEqual(combined_ast.type, "operator")  # Check if root is an operator
        # You can add more assertions to check the structure of the combined AST

    def test_evaluate_rule(self):
        ast = create_rule("age > 30 AND salary > 50000")
        data = {"age": 35, "salary": 60000}
        result = evaluate_rule(ast, data)
        
        self.assertTrue(result)  # Check if the evaluation returns True

        data = {"age": 25, "salary": 60000}
        result = evaluate_rule(ast, data)
        
        self.assertFalse(result)  # Check if the evaluation returns False

if __name__ == '__main__':
    unittest.main()