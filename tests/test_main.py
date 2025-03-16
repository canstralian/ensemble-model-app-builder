import pytest
from unittest.mock import patch, MagicMock
from main import generate_app_code


# Mock the API response to avoid actual API calls during testing
@pytest.fixture
def mock_genai():
    with patch("google.generativeai.GenerativeModel") as mock_model:
        mock_instance = MagicMock()
        mock_response = MagicMock()
        mock_response.text = (
            "# Generated app code\nimport streamlit as st\n\nst.title('Test App')"
        )
        mock_instance.generate_content.return_value = mock_response
        mock_model.return_value = mock_instance
        yield mock_model


# Test for valid input
def test_generate_app_code_valid(mock_genai):
    result = generate_app_code("Streamlit", "Test App")
    assert "# Generated app code" in result
    assert "import streamlit as st" in result


# Test for API error
def test_generate_app_code_api_error():
    with patch("google.generativeai.GenerativeModel") as mock_model:
        mock_instance = MagicMock()
        mock_instance.generate_content.side_effect = Exception("API Error")
        mock_model.return_value = mock_instance

        result = generate_app_code("Streamlit", "Test App")
        assert "An error occurred" in result


# Test with no API key configured
def test_generate_app_code_no_api():
    with (
        patch("main.api_key", None),
        patch("main.st.session_state.get") as mock_session,
    ):
        mock_session.return_value = None
        result = generate_app_code("Streamlit", "Test App")
        assert "API key not configured" in result
