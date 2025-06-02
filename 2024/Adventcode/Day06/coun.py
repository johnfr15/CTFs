import requests
import math
import numpy as np 

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_map():
    res = requests.get("https://adventofcode.com/2024/day/6/input", cookies=COOKIES)
    text = res.text
    print(text.count("#"))
    map = [[c for c in line] for line in text.split("\n")]
    map.pop()

    return map

# Function to find the character in the matrix
def find_character(matrix, target) -> np.ndarray:
    for row_index, row in enumerate(matrix):
        for col_index, char in enumerate(row):
            if char == target:
                return np.array([row_index, col_index])  # Return the position as (row, column)
    return None

def is_out(map, pos: np.ndarray):
    rowlen = len(map)
    collen = len(map[0])
    return pos[0] >= collen or pos[0] < 0 or pos[1] >= rowlen or pos[1] < 0 

def rotate(d: np.ndarray) -> np.ndarray:
    if d[0] == 0 and d[1] == 1:
        return np.array([1,0])
    if d[0] == 1 and d[1] == 0:
        return np.array([0,-1])
    if d[0] == 0 and d[1] == -1:
        return np.array([-1,0])
    
    return np.array([0,1])

def is_obs(map, pos: np.ndarray) -> bool:
    try:
        return map[pos[0]][pos[1]] == "#"
    except Exception:
        return False

def is_marked(map, pos: np.ndarray) -> bool:
    return map[pos[0]][pos[1]] == "X"

def print_map(map):
    [ print(''.join(line)) for line in map ]

def solve(map):
    start = find_character(map, "^")
    if start is None:
        print("Start position not found!")
        return
    
    pos = start
    direction = np.array([-1,0])
    n = 0

    while not is_out(map, pos):
        
        if not is_marked(map, pos):
            n+=1
            map[pos[0]][pos[1]] = "X"
        if is_obs(map, pos + direction):
            direction = rotate(direction)
        pos = pos + direction

    print_map(map)

    return n
    
    


if __name__ == "__main__":
    map = get_map()
    