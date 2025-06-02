import requests
import re

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_memory():
    res = requests.get("https://adventofcode.com/2024/day/3/input", cookies=COOKIES)
    memory = res.text
    return memory

def solve(valids: list[str]):
    n = 0
    for v in valids:
        idx = v.index(',')
        n1 = int(''.join(v[4:idx]))
        n2 = int(''.join(v[idx+1:-1]))
        n += n1 * n2
    return n



if __name__ == "__main__":
    memo = get_memory()

    pattern = r'\bmul\(\d{1,3},\d{1,3}\)'
    valids = re.findall(pattern, memo)

    total = solve(valids)
    print( "total: ", total)