import requests

def get_data(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        data = response.json()  # Parse JSON response
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

url = "https://ecommerce-data-generator.onrender.com"
params = {"year": "2020", "month": "2", "day": "3", "hour":"4", "country":"fr"}

result = get_data(url, params=params)

if result:
    print("API request successful!")
    print(result)
else:
    print("API request failed.")


if __name__ == "__main__":
    get_data(url, params=params)