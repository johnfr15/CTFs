flag = open("output.txt").read()
assert len(flag) == 64

sep = len(flag) // 2
y = "".join([ x + y for x, y in zip(flag[sep:], flag[:sep])])


for i in range(8):
    y = "".join([
        y[-8::-8],
        y[-7::-8],
        y[-6::-8],
        y[-5::-8],
        y[-4::-8],
        y[-3::-8],
        y[-2::-8],
        y[-1::-8],
    ])
    print(y)