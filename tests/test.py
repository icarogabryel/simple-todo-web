import requests

def send_get_request(path):
    url = f"http://localhost:8080{path}"
    try:
        response = requests.get(url)
        print(f"Response from {url}:")
        print(f"Status Code: {response.status_code}")
        print(f"Body: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Test different paths
    send_get_request("/")       # Root path
    send_get_request("/hello")  # /hello path
    send_get_request("/goodbye")  # /goodbye path
    send_get_request("/unknown")  # Unknown path
