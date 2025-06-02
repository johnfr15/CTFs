import requests
import numpy as np 

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_map():
    res = requests.get("https://adventofcode.com/2024/day/8/input", cookies=COOKIES)
    lines = res.text.split('\n')
    lines.pop()

    map = [[c for c in l] for l in lines]

    return map

def print_map(map):
    [ print(''.join(line)) for line in map ]



ANTINODES = get_map()
ANTINODES = [['.' for _ in range(len(ANTINODES[0]))] for _ in range(len(ANTINODES))]




def isout(map: list[list[str]], pos: np.ndarray):
    rowlen = len(map)
    collen = len(map[0])
    return pos[0] >= collen or pos[0] < 0 or pos[1] >= rowlen or pos[1] < 0 

def isfree(map, pos: np.ndarray):
    return map[pos[0]][pos[1]] == "."

def find_next(map: list[list[str]], start: np.ndarray, antenna: str):
    pos = start.copy()

    while not isout(map, pos):
        if map[pos[0]][pos[1]] == antenna:
            return pos
        
        nextpos(map, pos)
        
    return False

def nextpos(map, pos: np.ndarray):
    pos[1] += 1
    if isout(map, pos):
        pos[0] += 1
        pos[1] = 0



def put_antinodes(map: list[list[str]], antena: np.ndarray, antenachar: str):

    pos = antena.copy()
    nextpos(map, pos)

    counter = 0
    while not isinstance(find_next(map, pos, antenachar), bool):
        antena2 = find_next(map, pos, antenachar)
        diff = antena2 - antena

        if isfree(ANTINODES, antena):
            ANTINODES[antena[0]][antena[1]] = '#'
            counter += 1
        if isfree(ANTINODES, antena2):
            ANTINODES[antena2[0]][antena2[1]] = '#'
            counter += 1
            
        inverse = antena-diff
        projection = antena2+diff
        while not isout(map, inverse):
            if isfree(ANTINODES, inverse):
                ANTINODES[inverse[0]][inverse[1]] = '#'
                counter += 1
            inverse -= diff
        while not isout(map, projection): 
            if isfree(ANTINODES, projection):
                ANTINODES[projection[0]][projection[1]] = '#'
                counter += 1
            projection += diff

        pos = antena2
        nextpos(map, pos)

    return counter



def solve(map: list[list[str]], antenas: list[str]):

    antinodes = 0
    pos = np.array([0,0])
    while not isout(map, pos):

        el = map[pos[0]][pos[1]]
        if el in antenas:
            n = put_antinodes(map, pos, el)
            antinodes += n

        nextpos(map, pos)

    return antinodes


if __name__ == "__main__":
    map = get_map()
   
    antenas = set("".join(["".join(l) for l in map]))
    antenas.remove(".")

    print( solve(map, antenas) )
