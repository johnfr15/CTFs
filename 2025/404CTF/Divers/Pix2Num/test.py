import sys

# Autorise les conversions de très longues chaînes
sys.set_int_max_str_digits(100000)

# Lecture du nombre décimal
with open('./number.txt', 'r') as f:
    dec_str = f.read().strip()

# Conversion en hexadécimal, suppression du '0x'
hex_str = hex(int(dec_str, 10))[2:]

# Si la longueur est impaire, on préfixe par '0' pour avoir un nombre paire de caractères
if len(hex_str) % 2:
    hex_str = '0' + hex_str

# Reconstruction des bytes
data = bytes.fromhex(hex_str)

# Affichage (ou redirection dans test.out)
print(data)
