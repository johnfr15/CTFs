import base64
from urllib.parse import unquote

# Encoded strings and the order
encoded_strings = ["L2cz", "YmxfR1g=", "ZE1OTQ==", "TkROeQ==", "WF9V"]
order = [0, 2, 3, 1, 4]

# Function to decode each Base64 string
def decode_string(encoded):
    # Decode Base64
    decoded_base64 = base64.b64decode(encoded).decode('utf-8')
    # Convert to URL-decoded string
    return unquote(''.join(f'%{ord(c):02x}' for c in decoded_base64))

# Build the secret path
secret_path = "".join(decode_string(encoded_strings[i]) for i in order)

# Print the secret path
print("Secret Path:", secret_path)

