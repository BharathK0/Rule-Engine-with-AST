# Rule Engine Application

## Overview
This is a simple rule engine application that uses an Abstract Syntax Tree (AST) to evaluate user eligibility based on various attributes such as age, department, salary, and experience. The application consists of a 3-tier architecture: a simple UI, an API, and a backend data layer.

## Features
- Create rules using a string format
- Combine multiple rules into a single AST
- Evaluate rules against user attributes
- Sample data for testing

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/rule_engine.git
    cd rule_engine
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```bash
    python -m app.api
    ```

2. Use the API endpoints to create, combine, and evaluate rules.

## API Endpoints
- `POST /create_rule`: Creates a rule from a string.
- `POST /combine_rules`: Combines multiple rules into a single AST.
- `POST /evaluate_rule`: Evaluates a rule against provided user attributes.

## Sample Data
Sample user data is available in `data/sample_data.json`. You can use this data to test the rule evaluations.

## Testing
Run the test suite using:
```bash
python -m unittest discover tests/
```

## License
This project is licensed under the MIT License.

### Explanation:
- **Overview:** A brief description of what the project does.
- **Features:** Lists the main features of the application.
- **Installation:** Instructions for setting up the project on a local machine.
- **Usage:** How to run the application and interact with the API.
- **API Endpoints:** A summary of available API endpoints and their functions.
- **Sample Data:** Information about the sample data used for testing.
- **Testing:** Instructions on how to run tests.
- **License:** Include licensing information if applicable.

### Conclusion
These files will help structure your project and provide essential information and functionality.



























































