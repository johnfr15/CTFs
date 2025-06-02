import requests
import math
import numpy as np 
import itertools

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_bridge():
    res = requests.get("https://adventofcode.com/2024/day/7/input", cookies=COOKIES)
    lines = res.text.split('\n')
    lines.pop()

    results = [int(l.split(':')[0]) for l in lines]
    calcs = [l.split(':')[1].strip().split(" ") for l in lines]

    return results, calcs


def find(res: int, calc: list[str], i: int):
    print(f"finding {i}")
    operators = ['+', '*', "||"]

    op_comb = itertools.product(operators, repeat=len(calc) - 1)

    for op in list(op_comb):
        expression = list(itertools.chain(*zip(calc, op + ('',), strict=True)))
        n = expression[0]
        for idx in range(1, len(expression)-1, 2):
            if expression[idx] == "||":
                n = int(str(n) + expression[idx+1])
            else:
                n = eval("".join([str(n), expression[idx], expression[idx+1]]))

        if res == n: return res
    return None


if __name__ == "__main__":
    res, calcs  = get_bridge()
   
    matchs = [ find(res[idx], c, idx) for idx, c in enumerate(calcs)]
    matchs = [n for n in matchs if n is not None]
    print(matchs)

    print(sum(matchs))