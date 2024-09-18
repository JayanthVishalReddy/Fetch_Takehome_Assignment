import requests
import yaml
import time
from collections import defaultdict

def load_config(file_path):
    """Load YAML configuration from the specified file path."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def test_endpoint(endpoint):
    """Test the health of an endpoint and return if it's UP or DOWN."""
    url = endpoint.get('url')
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    try:
        response = requests.request(method, url, headers=headers, data=body, timeout=0.5)
        # Check if the response code is 2xx and latency is less than 500 ms.
        is_up = 200 <= response.status_code < 300 and response.elapsed.total_seconds() < 0.5
    except requests.RequestException:
        is_up = False

    return is_up

def main():
    """Main function to load config, test endpoints, and log results."""
    # Hardcoded path to the YAML configuration file.
    config_path = "endpoints.yml"
    config = load_config(config_path)
    results = defaultdict(list)

    try:
        while True:
            start_time = time.time()
            print("Starting a new test cycle...")
            
            for endpoint in config:
                domain = endpoint['url'].split('/')[2]  # Extract domain from URL.
                is_up = test_endpoint(endpoint)
                results[domain].append(is_up)

            # Calculate and log availability percentages.
            for domain, outcomes in results.items():
                availability = 100 * sum(outcomes) / len(outcomes)
                print(f"{domain} has {availability:.0f}% availability percentage")

            # Sleep until 15 seconds have passed since start_time.
            time.sleep(max(0, 15 - (time.time() - start_time)))

    except KeyboardInterrupt:
        print("Program exited by user.")

if __name__ == "__main__":
    main()