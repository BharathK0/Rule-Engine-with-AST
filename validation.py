def is_valid_rule(rule):
    """
    Validate if the rule is syntactically correct.
    A simple example could be checking if the rule is a non-empty string.
    """
    if not isinstance(rule, str) or not rule.strip():
        return False
    # Add more complex rule validation logic here
    return True

def is_valid_attribute(attribute, criteria):
    """
    Validate if the attribute meets the defined criteria.
    """
    if not isinstance(attribute, dict):
        return False
    
    for key, value in criteria.items():
        if key not in attribute or not isinstance(attribute[key], value):
            return False
    
    return True

# Example usage
rule = "example_rule"
attribute = {"name": "example", "value": 10}
criteria = {"name": str, "value": int}

print(is_valid_rule(rule))  # Should return True
print(is_valid_attribute(attribute, criteria))  # Should return True