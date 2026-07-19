# Python Utils 42

Python Utils 42 is a collection of general-purpose utilities designed to simplify common tasks in Python programming. With easy-to-use functions and classes, this library aims to enhance productivity and streamline your workflow in various applications.

## Features

- **Data Validation**: Easily validate inputs with reusable validation functions for strings, lists, and more.
- **File Operations**: Simplified file handling with functions to read, write, and manipulate files in various formats (CSV, JSON, etc.).
- **Networking Utilities**: Tools for quick HTTP requests, parsing responses, and managing API interactions seamlessly.
- **Logging Enhancements**: A customizable logging class that integrates with standard Python logging for better debugging experiences.

## Installation

To install Python Utils 42, use pip. Open your terminal and run the following command:

```bash
pip install python-utils-42
```

## Basic Usage Example

Here’s a quick example to demonstrate how to use the Data Validation and File Operations utilities:

```python
from python_utils_42 import Validator, FileHandler

# Data Validation Example
input_data = "test@example.com"
if Validator.is_valid_email(input_data):
    print(f"{input_data} is a valid email.")
else:
    print(f"{input_data} is NOT a valid email.")

# File Operations Example
file_path = 'data/sample.json'
data = {"name": "John Doe", "age": 30}
FileHandler.write_json(file_path, data)

# Read the written file
read_data = FileHandler.read_json(file_path)
print("Data read from file:", read_data)
```

## License

![MIT License](https://img.shields.io/badge/license-MIT-green)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.