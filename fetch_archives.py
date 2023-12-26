import requests

def fetch_archives(year, month, api_key):
    """
    Fetches news archive for a specific year and month from the New York Times Archive API.

    Args:
    year (int): Year of the archive.
    month (int): Month of the archive.
    api_key (str): API key for authenticating with the New York Times API.

    Returns:
    dict: JSON response containing the archive data.
    """
    url = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json"
    params = {'api-key': api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

# Example usage
# api_key = "your_api_key_here"
# archive_data = get_nyt_archive(2020, 1, api_key)
