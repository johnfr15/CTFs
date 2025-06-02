import requests
import numpy as np 

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_map():
    res = requests.get("https://adventofcode.com/2024/day/9/input", cookies=COOKIES)
    # res = ""
    # with open("map.txt", "r") as f:
    #     res = f.read()
    return res.text

def parse_file(file: str):
    pfile = []
    for idx, el in enumerate([(file[i], file[i+1]) for i in range(0, len(file)-1, 2)]):
        arr1 =  [idx for _ in range(int(el[0]))]
        pfile.extend(arr1)
        if el[1] == "\n": break
        arr2 = ["." for _ in range(int(el[1]))] 
        pfile.extend(arr2)
    return pfile

def count_free_space(idx: int, pfile: list[str]):
    i = 0
    while pfile[idx+i] == '.':
        i += 1
    return i

def count_file_size(idx: int, pfile: list[str], n: str):
    i = 0
    while idx-i >= 0 and pfile[idx-i] == n:
        i += 1
    return i

def nextstart(pfile):
    i = 0
    while pfile[i] != '.': i+= 1
    return i

def solve(pfile: list[str]):
    hasmoved = []
    cfile = [el for el in pfile] 
    j = len(pfile) - 1

    start = 0
    duetomoved = False

    while True:
        start = nextstart(cfile)
        while cfile[j] == ".": j -= 1
        if j <= start: break

        i = start
        while i < j:
            while cfile[i] != '.': i+= 1

            n = cfile[j]
            if n in hasmoved:
                while cfile[j] == n:
                    j -= 1
                duetomoved = True
                break

            fs = count_free_space(i, cfile)
            blk = count_file_size(j, cfile, n)
        

            if blk <= fs:
                while cfile[j] == n:
                    cfile[i] = cfile[j] 
                    cfile[j] = '.'
                    i += 1
                    j -= 1
                hasmoved.append(n)
                break
            else:
                while cfile[i] == ".": 
                    i += 1

        if duetomoved:
            duetomoved = False
        elif i >= j:
            while cfile[j] != '.':
                j -= 1
    print(f"last start {start}: {cfile[start-1]}" )        
    print(cfile)
    return sum([idx * int(el) for idx, el in enumerate(cfile) if el != '.'])



if __name__ == "__main__":
    file = get_map()
    pfile = parse_file(file)
    test = ["0","0",".",".",".","1","1","1",".",".",".","2",".",".",".","3","3","3",".","4","4",".","5","5","5","5",".","6","6","6","6",".","7","7","7",".","8","8","8","8","9","9"]

    print(solve(pfile))