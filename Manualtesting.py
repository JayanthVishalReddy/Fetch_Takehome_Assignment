import requests
from collections import defaultdict
import time


endpoints = [
    {
        "url": "https://fetch.com/",
        "method": "GET"
    },
    {
        "url": "https://fetch.com/careers",
        "method": "GET"
    },
    {
        "url": "https://fetch.com/some/post/endpoint",
        "method": "POST",  
        "headers": {"Content-Type": "application/json"},  
        "body": '{"key": "value"}'  
    },
    {
        "url": "https://www.fetchrewards.com/",
        "method": "GET"
    }
]


test_rounds = 3

sleep_time = 5  

def test_endpoint(endpoint):
    """Test an endpoint and return if it's UP or DOWN, with debug prints."""
    url = endpoint["url"]
    method = endpoint["method"]
    headers = endpoint.get("headers", {})
    body = endpoint.get("body", None)

    print(f"Testing {method} request for {url}")
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=0.5)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=body, timeout=0.5)
        response_time = response.elapsed.total_seconds() * 1000  
        is_up = 200 <= response.status_code < 300 and response_time < 500
        print(f"Status Code: {response.status_code}, Response Time: {response_time} ms, Result: {'UP' if is_up else 'DOWN'}")
        return is_up
    except requests.RequestException as e:
        print(f"Failed to reach {url}: {str(e)}")
        return False

def main():
    """Run tests on endpoints and log availability, with debug prints."""
    print("Script started")
    results = defaultdict(list)

    for _ in range(test_rounds):
        for endpoint in endpoints:
            is_up = test_endpoint(endpoint)
            results[endpoint['url']].append(is_up)
        print("Sleeping between rounds...")
        time.sleep(sleep_time)

    
    print("Calculating availability percentages...")
    for url, outcomes in results.items():
        availability = 100 * sum(outcomes) / len(outcomes)
        print(f"{url} has {availability:.0f}% availability percentage")
    print("Script ended")

if __name__ == "__main__":
    main()