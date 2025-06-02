charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}-!"
n = len(charset)  # 65

reverse_lookup = {}
for x in range(n):
    y = pow(2, x, n+1)
    reverse_lookup[y] = x

encrypted = "828x6Yvx2sOnzMM4nI2sQ"
flag = ""
for c in encrypted:
    y = charset.index(c)
    x = reverse_lookup.get(y, None)
    if x is not None:
        flag += charset[x]
    else:
        flag += "?"

print(flag)
