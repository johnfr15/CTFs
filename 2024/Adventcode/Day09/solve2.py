import requests
import numpy as np 

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_map():
    # res = requests.get("https://adventofcode.com/2024/day/9/input", cookies=COOKIES)
    res = ""
    with open("map.txt", "r") as f:
        res = f.read()
    return res

def parse_file(file: str):
    pfile = []
    for idx, el in enumerate([(file[i], file[i+1]) for i in range(0, len(file)-1, 2)]):
        arr1 =  [idx for _ in range(int(el[0]))]
        pfile.extend(arr1)
        if el[1] == "\n": break
        arr2 = ["." for _ in range(int(el[1]))] 
        pfile.extend(arr2)
    return pfile

def solve(pfile):
    i = 0
    cfile = []

    for idx, el in enumerate(pfile[::-1]):
        j = (len(pfile)-1) - idx
        if i > j: break

        if el == ".": continue
        while pfile[i] != ".":
            if i >= j: break
            cfile.extend( [int(pfile[i])] )
            i += 1

        cfile.extend([el])
        i += 1
    print(cfile)
    return sum([idx * el for idx, el in enumerate(cfile)])

if __name__ == "__main__":
    file = get_map()
    pfile = parse_file(file)


    print(solve(pfile))