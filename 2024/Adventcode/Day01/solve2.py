import requests

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_pairs() -> tuple[int, int]:
    res = requests.get("https://adventofcode.com/2024/day/1/input", cookies=COOKIES)
    lines = res.text.split("\n")
    lines = [ line.split(" ") for line in lines ]
    lines = [list(filter(None, line)) for line in lines]
    lines.pop()

    pairs = [ (int(line[0]), int(line[1])) for line in lines ]
    return pairs

def solve(pairs: list[tuple[int,int]]) -> int:

    ls = [ pair[0] for pair in pairs ]
    rs = [ pair[1] for pair in pairs ]

    similars = [ n * rs.count(n) for n in ls ]

    return sum(similars)



if __name__ == "__main__":
    pairs = get_pairs()
    total = solve(pairs)

    print("total: ", total)