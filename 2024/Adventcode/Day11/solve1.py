import requests
import numpy as np 
from multiprocessing import Pool
from collections import Counter

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_stones():
    # res = requests.get("https://adventofcode.com/2024/day/11/input", cookies=COOKIES)
    with open("res40.txt", "r") as f:
        res = f.read() 
    res = res.split("  ")
    res.pop()
    print(res[-1])

    return res

class Eleven():
    stones: list[str]

    def __init__(self, stones: list[str]):
        self.stones = stones
        

    def get_stones(self):
        return self.stones

    def blink(self, stones: list[str]):
        stones = [ self._process_stone(s) for s in stones ]
        return [item for sublist in stones for item in sublist]

    def _process_stone(self, stone: str) -> list[str]:
        if stone == '0': return ['1']

        if len(stone) % 2 == 0: 
            half = int(len(stone)/2)
            left = str(int(stone[:half]))
            right = str(int(stone[half:]))
            return [left, right]
        
        return [str(int(stone) * 2024)]


def split_chunks(data, num_chunks):
    """Split the data evenly into num_chunks."""
    chunk_size = len(data) // num_chunks
    return [data[i * chunk_size: (i + 1) * chunk_size] for i in range(num_chunks)] + \
           ([] if len(data) % num_chunks == 0 else [data[num_chunks * chunk_size:]])

def worker(chunk):
    """Wrapper function for processing a chunk."""
    chall = Eleven([])
    return chall.blink(chunk)

if __name__ == "__main__":
    stones = get_stones() 
    chall = Eleven(stones)
    
    memoize15 = {}
    memoize20 = {}
    memoize35 = {}

    lengthd = {}  
    i = 0
    print("Total unniq key: ", len(set(stones)))
    for idx, s in enumerate(set(stones)):
        print(f"memoize {idx} => {s}")
        tmp = [s]
        for i in range(20):
            if i == 15:
                memoize15[s] = tmp
            tmp = chall.blink(tmp)
        memoize20[s] = tmp
    
    print("Calculate memo35")
    for idx, s in enumerate(set(stones)):
        memo20 = memoize20[s]

        memo35 = []
        for num in memo20:
            memo = memoize15.get(num, None)
            if memo is None:
                print("Find memo15 of ", num)
                find = [num]
                for i in range(15):
                    find = chall.blink(find)
                memoize15[num] = find
        M20 = Counter(memo20)
        [ memo35.extend(memoize15[k] * v) for k, v in M20.items()]
        memoize35[s] = memo35

    
    print("Counting")
    C = Counter(stones)
    print( sum([ len(memoize35[k]) * v for k, v in C.items() ]) )
