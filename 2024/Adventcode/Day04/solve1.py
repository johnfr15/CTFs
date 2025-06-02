import requests
import re

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_puzzle():
    res = requests.get("https://adventofcode.com/2024/day/4/input", cookies=COOKIES)
    puzzle = res.text
    puzzle = [ list(line) for line in puzzle.split("\n")]
    puzzle.pop()
    return puzzle


# Check for "MAS" in up, down, left, right directions
def udlr(x, y, puzzle):
    n = 0
    rows, cols = len(puzzle), len(puzzle[0])
    if y+1 < cols and y-1 >= 0   and puzzle[x][y+1] == "M" and puzzle[x][y-1] == "S": n += 1
    if y-1 >= 0   and y+1 < cols and puzzle[x][y-1] == "M" and puzzle[x][y+1] == "S": n += 1
    if x+1 < rows and x-1 >= 0   and puzzle[x-1][y] == "M" and puzzle[x+1][y] == "S": n += 1
    if x-1 >= 0   and x+1 < rows and puzzle[x+1][y] == "M" and puzzle[x-1][y] == "S": n += 1
    return n

# Check for "MAS" in diagonal directions
def diags(x, y, puzzle):
    n = 0
    rows, cols = len(puzzle), len(puzzle[0])
    if x+1 < rows and y+1 < cols and x-1 >= 0   and y-1 >= 0    and puzzle[x+1][y+1] == "M" and puzzle[x-1][y-1] == "S": n += 1
    if x-1 >= 0   and y-1 >= 0   and x+1 < rows and y+1 < cols  and puzzle[x-1][y-1] == "M" and puzzle[x+1][y+1] == "S": n += 1
    if x+1 < rows and y-1 >= 0   and x-1 >= 0   and y+1 < cols  and puzzle[x+1][y-1] == "M" and puzzle[x-1][y+1] == "S": n += 1
    if x-1 >= 0   and y+1 < cols and x+1 < rows and y-1 >= 0    and puzzle[x-1][y+1] == "M" and puzzle[x+1][y-1] == "S": n += 1
    return n

def is_xmas(x,y,puzzle):
    return diags(x,y,puzzle) >= 2

def solve(puzzle):
    c = 0
    xlen = len(puzzle[0])

    x = 0
    y = 0
    while y < len(puzzle):
        if puzzle[x][y] == "A" and is_xmas(x,y,puzzle): 
            c += 1

        if (x+1) == xlen:
            x = 0
            y += 1
        else:
            x += 1
    return c


if __name__ == "__main__":
    puzzle = get_puzzle()
    res = solve(puzzle)

    print("res: ", res)