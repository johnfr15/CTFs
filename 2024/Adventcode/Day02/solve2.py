import requests

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_reports():
    res = requests.get("https://adventofcode.com/2024/day/2/input", cookies=COOKIES)
    lines = res.text.split("\n")
    lines = [ line.split(" ") for line in lines ]
    lines.pop()

    pairs = [ [int(e) for e in line] for line in lines ]
    return pairs

def is_sorted(lst: list[int]) -> bool:
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def solve(reports: list[list[int]]):
    safe = 0
    
    for report in reports:
        if is_sorted(report):
            diff = [ abs(report[i-1] - report[i]) for i in range(1, len(report)) ]
            maximum = max(diff)
            minimum = min(diff)
            if maximum < 4 and minimum > 0:
                safe += 1

    return safe


if __name__ == "__main__":
    reports = get_reports()
    print( "safe: ", solve(reports))