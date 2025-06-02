# List of encrypted flags (as hex strings)
XLINES = [
    # '43794c9c8faa2cff24edc8afe507a13f62837c7e166f428cab5aff893225ff19104bc8754c1c09',
    # '5d315e8786e62cf763e9d4afe80ca13b649a717e11615986b642f3952f76b71b0342c4',
    # '46785a8bcae62aeb60a5deeef107a1256ed7792752695886ff50f5886171ff1717',
    # '5d315e819fe621b966e08dfae906e43a78837b31162e5e8cff46e8953275f20a0d5ad23d4712144c',
    # '557f4dce9ee220b967e4dfffe616e9216a9934291b7d5690bb45ba922e6afc',
    '55315a868fef35f16beac6afe810a1206a81717e1e6b5690b152ba953462ff0c424acd6e0307055a81b93590c1fe',
    # '557d489dcafd2df870a5cfe0e816f268628334291b7a5fc2aa58f99f3276f616160fc27c5116',
    # '557f4dce8bee21fc24f1c5eaa712ee3f6e853431142e448db216fb9e2b70e5110c48816b46011e5a',
    '407e099783ef29fd24edc4fca704f33d6283343f1c6a178ab645ba962464f1581147c0714f530350d5f53690dee6',
    # '40785ace93e530b970edccfba711e0312b9e607e1c6143c2b616e3953425f317425bc9780317085ac5a6',
    '41754a9a8cf13da976dac4e1d810b1253f994b6f47514387b106e8a57175a40a0370d22c4d14084d9ea8aa',
]

# Define the known flag format, which is part of the k       |   n flag pattern.
known_flag_format = b'4\x11)\xee\xea\x8aE\x99\x04\x85\xad\x8f\x87\x62\x81\x48\x0b\xf7\x14\x5e\x72\x0e\x37\xe2\xdf\x36\x9a\xfa\x41\x05\x97\x78\x62\x2f\xa1\x1d\x23\x73\x6d\x3f\xa1\xd50'
idx = 42

# Loop over each encrypted line
for LINE in XLINES:
    flag_bytes = bytes.fromhex(LINE)
    
    # We are focusing on the 7th byte (index 6), which we will manually guess by XOR'ing with each byte from 0 to 255
    for guess in range(256):
        # XOR the 7th byte (index 6) with the guess byte (from 0 to 255)
        guessed_byte = flag_bytes[idx] ^ guess
        
        # if chr(guessed_byte) == ' ': 
        # print(f"guess[{idx}]: {hex(guess)}")
        # Construct the decrypted flag with the guessed 7th byte
        if (chr(guessed_byte) > 'a' and chr(guessed_byte) < 'z') or chr(guessed_byte) == ' ':
            decrypted_flag = bytes([b ^ known_flag_format[i % idx] for i, b in enumerate(flag_bytes[:idx])]) + bytes([guessed_byte]) + flag_bytes[idx+1:]
            # Print the decrypted flag with the guessed byte and its corresponding ASCII character
            print(hex(guess), decrypted_flag)
    print()
