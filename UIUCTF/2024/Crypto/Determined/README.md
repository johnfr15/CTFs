# 1

## gen.py: Step-by-Step RSA Decryption

```python
from Crypto.Util.number import long_to_bytes, inverse

# Given values
n = 158794636700752922781275926476194117856757725604680390949164778150869764326023702391967976086363365534718230514141547968577753309521188288428236024251993839560087229636799779157903650823700424848036276986652311165197569877428810358366358203174595667453056843209344115949077094799081260298678936223331932826351
e = 65535
c = 72186625991702159773441286864850566837138114624570350089877959520356759693054091827950124758916323653021925443200239303328819702117245200182521971965172749321771266746783797202515535351816124885833031875091162736190721470393029924557370228547165074694258453101355875242872797209141366404264775972151904835111

# Obtained from factorization or provided secret
p = ...  # Factorization result
q = ...  # Factorization result

# Compute phi(n)
phi_n = (p - 1) * (q - 1)

# Compute the private exponent d
d = inverse(e, phi_n)

# Decrypt the ciphertext
m = pow(c, d, n)

# Convert m back to bytes to recover the FLAG
flag = long_to_bytes(m)
print(flag)

```