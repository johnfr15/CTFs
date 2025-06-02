import requests
import random
import string

def generate_random_payload(length):
    """Generate a random payload of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def fuzz_endpoint_random(base_url, param_name, num_requests=10, max_payload_length=50):
    """Fuzz the endpoint with randomly generated payloads."""
    for i in range(num_requests):
        # Generate a random length between 1 and max_payload_length
        payload_length = random.randint(1, max_payload_length)
        payload = generate_random_payload(payload_length)
        url = f"{base_url}?{param_name}={payload}"
        print(f"Fuzzing with payload: {payload}")
        
        try:
            response = requests.get(
                url,
                headers={
                    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": "\"Linux\"",
                    "Accept-Language": "en-US",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Priority": "u=0, i",
                    "Connection": "keep-alive"
                }
            )
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Body: {response.text[:200]}... (truncated)\n")  # Print a snippet of the response for readability
        except Exception as e:
            print(f"An error occurred with payload {payload}: {e}\n")

# Example usage
base_url = "https://55nlig2es7hyrhvzcxzboyp4xe0nzjrc.lambda-url.us-east-1.on.aws/"
param_name = "payload"
fuzz_endpoint_random(base_url, param_name, num_requests=20, max_payload_length=100)
