import ast

def create_rule(rule_string):
    """
    Parse the rule string and construct the corresponding AST.
    """
    try:
        rule_ast = ast.parse(rule_string, mode='eval')
        return rule_ast
    except SyntaxError as e:
        print(f"Syntax error in rule: {e}")
        return None

def combine_rules(rules):
    """
    Combine multiple rules into a single AST.
    """
    combined_expr = " and ".join(f"({rule})" for rule in rules)
    return create_rule(combined_expr)

def evaluate_rule(rule_ast, data):
    """
    Evaluate the AST against given data.
    """
    try:
        compiled_rule = compile(rule_ast, filename="<ast>", mode="eval")
        return eval(compiled_rule, {}, data)
    except Exception as e:
        print(f"Error evaluating rule: {e}")
        return False

# Example usage
if __name__ == "__main__":
    rule1 = "data['age'] > 18"
    rule2 = "data['country'] == 'USA'"
    
    rule_ast1 = create_rule(rule1)
    rule_ast2 = create_rule(rule2)
    
    combined_rule_ast = combine_rules([rule1, rule2])
    
    data = {'age': 20, 'country': 'USA'}
    result = evaluate_rule(combined_rule_ast, data)
    print(f"Evaluation result: {result}")