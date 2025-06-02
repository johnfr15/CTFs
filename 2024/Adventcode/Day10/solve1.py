import requests
import numpy as np 

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_map():
    res = requests.get("https://adventofcode.com/2024/day/10/input", cookies=COOKIES)
    map = [[int(c) for c in line] for line in res.text.split('\n')]
    map.pop()

    return map

def isout(map: list[list[str]], pos: np.ndarray):
    rowlen = len(map)
    collen = len(map[0])
    return pos[0] >= collen or pos[0] < 0 or pos[1] >= rowlen or pos[1] < 0 


def count_trailhead(map, pos: np.ndarray, prev: np.ndarray, FOUND):
    curr = map[pos[0]][pos[1]]

    if isout(map, pos): return 0
    if curr == 9:
        FOUND[pos[0]][pos[1]] += 1
        return 0

    left    = np.copy(pos + np.array([0, -1])) if not np.array_equal(pos + np.array([0, -1]), prev) and not isout(map, (pos + np.array([0, -1]))) else None
    right   = np.copy(pos + np.array([0, 1]))  if not np.array_equal(pos + np.array([0, 1]),prev) and not isout(map, (pos + np.array([0, 1]))) else None
    up      = np.copy(pos + np.array([-1, 0])) if not np.array_equal(pos + np.array([-1, 0]), prev) and not isout(map, (pos + np.array([-1, 0]))) else None
    down    = np.copy(pos + np.array([1, 0]))  if not np.array_equal(pos + np.array([1, 0]), prev) and not isout(map, (pos + np.array([1, 0]))) else None
    
    c = 0
     
    if left  is not None and map[left[0]][left[1]] - curr == 1: c += count_trailhead(map, left, pos, FOUND)
    if right is not None and map[right[0]][right[1]] - curr == 1: c += count_trailhead(map, right, pos, FOUND)
    if up    is not None and map[up[0]][up[1]] - curr == 1: c += count_trailhead(map, up, pos, FOUND)
    if down  is not None and map[down[0]][down[1]] - curr == 1: c += count_trailhead(map, down, pos, FOUND)
    return c 

def nextpos(map, pos: np.ndarray):
    pos[1] += 1
    if isout(map, pos):
        pos[0] += 1
        pos[1] = 0

def solve(map):
    res = []
    pos = np.array([0, 0])

    while pos[0] < len(map):

        if map[pos[0]][pos[1]] != 0:
            nextpos(map, pos)
            continue

        FOUND = [[0 for _ in line] for line in get_map()]
        n_trailhead = count_trailhead(map, pos, None, FOUND)

        res.append(sum([ sum(line) for line in FOUND ]))
        nextpos(map, pos)

    print(res)
    return sum(res) 

        



if __name__ == "__main__":
    map = get_map()
    print(solve(map))

