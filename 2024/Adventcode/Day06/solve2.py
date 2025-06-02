import requests
import math
import numpy as np 

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_map():
    res = requests.get("https://adventofcode.com/2024/day/6/input", cookies=COOKIES)
    text = res.text
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
    








def get_next_hop(map, pos: np.ndarray, d: np.ndarray):
    while not is_out(map, pos):
        if is_obs(map, pos + d):
            d = rotate(d)
            return pos, d
        pos = pos + d
    return False

def can_loop(map, start: np.ndarray, direction: np.ndarray):
    
    pos = start.copy()
    d = direction.copy()
    nodes = dict()
    last_visited = []

    while not is_out(map, pos):
        while is_obs(map, pos + d):
            key = str((pos + d))
            if key not in nodes:
                nodes[key] = 0
            nodes[key] += 1
            last_visited = [nodes[key]] + last_visited[:3]
            if min(last_visited) == 10: 
                return True
            d = rotate(d)
       

        pos = pos + d
    return False

def set_obs(map, obs):
    map[obs[0]][obs[1]] = "#"
def unset_obs(map, obs):
    map[obs[0]][obs[1]] = "."
def already_visited(pos, v: dict):
    return v.get(str(pos)) is not None

def solve(map):
    start = find_character(map, "^")
    if start is None:
        print("Start position not found!")
        return
 
    pos = start
    direction = np.array([-1,0])
    visited = dict()
    visited[str(start)] = 1

    c = 0
    hopc = 1
    while True:
        
        pos_hop = pos.copy() 
        while not is_obs(map, pos_hop + direction) and not is_out(map, pos_hop+direction):
            pos_hop += direction
            # print(f"testing new obs {pos_hop}")
            set_obs(map, pos_hop)
            if not already_visited(pos_hop, visited) and can_loop(map, start, np.array([-1,0])):
                visited[str(pos_hop)] = 1
                c += 1
            unset_obs(map, pos_hop)
            

        hop = get_next_hop(map, pos, direction)
        hopc += 1
        if not hop:
            break
        pos = hop[0]
        direction = hop[1]

        print(f"hop {hopc}: {pos}")
    return c
    


if __name__ == "__main__":
    map = get_map()
 
    print(solve(map))




