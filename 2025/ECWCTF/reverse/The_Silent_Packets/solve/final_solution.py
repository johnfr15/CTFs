from hashlib import md5
from Cryptodome.Cipher import AES

def decrypt_blob():
    """Decrypt the encrypted blob"""
    print("[+] Step 1: Decrypting blob...")

    with open('logo_encrypted.jpg.enc', 'rb') as f:
        ciphertext = f.read()

    key = md5("bada55c0ffee".encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, b"\x00"*16)
    plaintext = cipher.decrypt(ciphertext)

    print(f"    Decrypted {len(plaintext)} bytes")
    print(f"    Key: {key.hex()}")

    return plaintext

def main():
    print("="*60)
    print("The Silent Packets - Final Solution")
    print("="*60)

    # Decrypt
    decrypted = decrypt_blob()

    # Save for inspection
    with open('final_decrypted.bin', 'wb') as f:
        f.write(decrypted)
    print("    Saved to: final_decrypted.bin")


if __name__ == '__main__':
    main()
