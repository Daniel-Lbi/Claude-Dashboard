import requests
import json
from datetime import datetime

def extract_data(api_url, params=None):
    """
    Extract data from a free API.
    
    Args:
        api_url (str): The API endpoint URL
        params (dict): Optional query parameters
    
    Returns:
        dict: JSON response from the API
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error extracting data: {e}")
        return None

# Example usage (replace with your chosen API)
if __name__ == "__main__":
    # Using JSONPlaceholder as an example
    api_url = "https://jsonplaceholder.typicode.com/posts"
    data = extract_data(api_url)
    if data:
        print(f"Extracted {len(data)} records")
        # Save raw data for inspection
        with open('../data/raw_data.json', 'w') as f:
            json.dump(data, f, indent=2)