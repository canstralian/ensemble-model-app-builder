import os
from typing import Optional

import requests


def use_huggingface_space(
    text_input: str, space_url: str, api_token: Optional[str] = None
) -> str:
    """
    Sends the provided text_input to a Hugging Face Space API for processing.

    Parameters:
    - text_input (str): The text to be processed by the Hugging Face Space.
    - space_url (str): The URL of the Hugging Face Space endpoint.
    - api_token (Optional[str]): Hugging Face API token for authenticated Spaces (default: None).

    Returns:
    - str: The response from the Hugging Face Space or an error message.
    """
    headers = {}
    if api_token:
        headers["Authorization"] = f"Bearer {api_token}"

    payload = {"data": [text_input]}

    try:
        response = requests.post(space_url, json=payload, headers=headers)
        response.raise_for_status()

        result = response.json()
        if (
            isinstance(result, dict)
            and "data" in result
            and isinstance(result["data"], list)
        ):
            return str(result["data"][0])
        elif isinstance(result, dict) and "output" in result:
            return str(result["output"])  # Handle different response format
        return "Unexpected response format."

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except KeyError:
        return "Unexpected response structure."


# Example usage:
if __name__ == "__main__":
    test_url = "https://<username>-<repo_name>.hf.space/run/predict"
    test_input = "Hello from Hugging Face Spaces!"

    # Retrieve the API key from Replit Secrets
    api_token = os.getenv("API_KEY")

    result = use_huggingface_space(test_input, test_url, api_token)
    print("Received output:", result)
