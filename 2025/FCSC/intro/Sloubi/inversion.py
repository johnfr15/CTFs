scrambled = "4B}mCuCNJmeVhvCzQusFHS7{2gCBCrQW"
flag = [''] * 32

for i in range(32):
    target_index = (i * 17 + 51) % 32
    flag[i] = scrambled[target_index]

print("".join(flag))
# The flag is: FCSC{