import requests
import math

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_puzzle():
    res = requests.get("https://adventofcode.com/2024/day/5/input", cookies=COOKIES)
    puzzle = res.text
    rules, updates = puzzle.split("\n\n")

    rules = rules.split("\n")
    tuples = [n.split("|") for n in rules]
    rules = {r[0]: [] for r in tuples}
    for t in tuples:
        rules[t[0]].append(t[1])

    updates = [ u.split(",") for u in updates.split("\n") ]
    updates.pop()

    return rules, updates

def is_ordered(rules: dict[str,str], lst: list[str]):
    for idx, el in enumerate(lst):
        for i in range(idx+1, len(lst)):
            if el in rules.get(lst[i], []): return False
    return True

def fix(rules: dict[str,str], lst: list[str]):
    i = 0
    j = 0
    while i < len(lst)-1:
        j = i+1
        while j < len(lst):
            if lst[i] in rules.get(lst[j], []):
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp
                j = i
            j+=1
        i+=1

    return lst

def solve(rules, updates):
    n = 0

    for u in updates:
        if is_ordered(rules,u):
            pass
        else:
            u = fix(rules,u)
            n += int(u[math.floor(len(u)/2)])
    return n
    


if __name__ == "__main__":
    rules, updates = get_puzzle()
    print(rules)
    print(solve(rules,updates))