from string import ascii_uppercase
cipher = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK".replace("'", " ").replace("\n", " ").split(" ")
alphabet = ascii_uppercase
plain = ""
shift = 2

for shift in range(26):
    plain = ""
    for word in cipher:
        for i in range(len(word)):
            plain += alphabet[(alphabet.index(word[i]) + shift) % len(alphabet)] if word[i] in alphabet else word[i]
        shift += 1
        plain += " "
    print(plain)
