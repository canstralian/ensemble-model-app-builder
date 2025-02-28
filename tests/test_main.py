import pytest
from main import generate_app_code  # Replace with the actual function you want to test

# Test for valid input
@pytest.mark.parametrize("input_data, expected_output", [
    ("Interactive Data Explorer", "expected code output for this task"),  # Add the realistic expected outputs
    ("Simple Linear Regression", "expected code output for this task"),
])
def test_function_to_test_valid(input_data, expected_output):
    assert generate_app_code("Streamlit", input_data) == expected_output

# Test for invalid input
@pytest.mark.parametrize("input_data", [
    None,  # Invalid case
    "",    # Invalid case
])
def test_function_to_test_invalid(input_data):
    with pytest.raises(ValueError):  # Adjust the exception type as needed
        generate_app_code("Streamlit", input_data)