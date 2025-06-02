import requests
import numpy as np 
from multiprocessing import Pool
from collections import Counter

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_garden():
    res = requests.get("https://adventofcode.com/2024/day/12/input", cookies=COOKIES)
    # with open("example2.txt", "r") as f:
    #     res = f.read()

    garden = res.text.split("\n")
    garden.pop()

    return [[p for p in l] for l in garden]

class Twelve():
    garden: list[list[str]]
    visited: list[list[str]]
    side: dict

    def __init__(self, garden: list[list[str]]):
        self.garden = garden
        self.visited = [['.' for p in l] for l in garden]
        self.visited2 = [['.' for p in l] for l in garden]
        self.side = dict()

    def get_cost(self) -> dict:
        cost = []
        for i in range(len(self.garden)):
            for j in range(len(self.garden[0])):
                pos = np.array([i,j])
                if not self._isvisited(pos):
                    region = self.garden[pos[0]][pos[1]]
                    [area, perimeter] = self._get_area_perimeter(pos, region)
                    cost.append( area * perimeter )
                
        return sum(cost)
    
    def get_cost2(self) -> dict:
        cost = []
        for i in range(len(self.garden)):
            for j in range(len(self.garden[0])):
                pos = np.array([i,j])
                if not self._isvisited(pos):
                    region = self.garden[pos[0]][pos[1]]
                    [area, perimeter] = self._get_area_perimeter(pos, region)
                    sides = self._follow_side(pos, np.array([0, 1]), region, None)
                    self.print_map(self.visited2)
                    print(f"{area}*{sides}={area*sides}")
                    print()
                    cost.append( area * sides )
        return sum(cost)
    
    def print_map(self, map):
        [ print(''.join(line)) for line in map ]




    #
    # PRIVATE
    #
    def _follow_side(self, pos: np.ndarray, direction: np.ndarray, region: str, start: np.ndarray) -> np.ndarray:
        if np.array_equal(pos, start) and np.array_equal(direction, np.array([0, 1])): 
            return 0
        if start is None: start = pos.copy()
        self.visited2[pos[0]][pos[1]] = "X"
        left  = self._get_left(direction)

        while True:
            if not self._isout(pos+left) and self._isregion(pos+left, region):
                self.visited2[pos[0]][pos[1]] = "X"
                direction = self.rotate_left(direction)
                return 1 + self._follow_side(pos+direction, direction, region, start)
            if self._isout(pos+direction) or self._isregion(pos+direction, region) == False:
                direction = self.rotate_right(direction)
                return 1 + self._follow_side(pos, direction, region, start)
            
            pos += direction
            self.visited2[pos[0]][pos[1]] = "X"
    


    def _get_area_perimeter(self, pos: np.ndarray, region: str) -> np.ndarray:
        if self._isout(pos) or self._isvisited(pos) or not self._isregion(pos, region): return np.array([0, 0])
        self.visited[pos[0]][pos[1]] = "X"
        
        left  = pos + np.array([0, -1]) 
        right = pos + np.array([0, 1])  
        up    = pos + np.array([-1, 0])
        down  = pos + np.array([1, 0])

        ap = np.array([1,0])

        if self._isout(left)  or self.garden[left[0]][left[1]] != region:   ap[1] += 1
        if self._isout(right) or self.garden[right[0]][right[1]] != region: ap[1] += 1 
        if self._isout(up)    or self.garden[up[0]][up[1]] != region:       ap[1] += 1 
        if self._isout(down)  or self.garden[down[0]][down[1]] != region:   ap[1] += 1
        return (ap 
            + self._get_area_perimeter(left, region)
            + self._get_area_perimeter(right, region)
            + self._get_area_perimeter(up, region)
            + self._get_area_perimeter(down, region)
        )


    def _get_left(self, d: np.ndarray):
        if d[0] == 1 and d[1] == 0: return np.array([0,1])
        if d[0] == -1 and d[1] == 0: return np.array([0,-1])
        if d[0] == 0 and d[1] == 1: return np.array([-1,0])
        return np.array([1,0])

    def rotate_left(self, d: np.ndarray) -> np.ndarray:
        if d[0] == 0 and d[1] == 1:
            return np.array([-1,0])
        if d[0] == 1 and d[1] == 0:
            return np.array([0,1])
        if d[0] == 0 and d[1] == -1:
            return np.array([1,0])
        return np.array([0,-1])
    
    def rotate_right(self, d: np.ndarray) -> np.ndarray:
        if d[0] == 0 and d[1] == 1:
            return np.array([1,0])
        if d[0] == 1 and d[1] == 0:
            return np.array([0,-1])
        if d[0] == 0 and d[1] == -1:
            return np.array([-1,0])
        return np.array([0,1])

    def _isout(self, pos: np.ndarray):
        rowlen = len(self.garden)
        collen = len(self.garden[0])
        return pos[1] >= collen or pos[0] < 0 or pos[0] >= rowlen or pos[1] < 0 
    
    def _isvisited(self, pos: np.ndarray):
        return self.visited[pos[0]][pos[1]] == "X"
    
    def _isregion(self, pos: np.ndarray, region: str):
        return self.garden[pos[0]][pos[1]] == region
    
    def _is_alone(self, pos, region):
        left  = pos + np.array([0, -1]) 
        right = pos + np.array([0, 1])  
        up    = pos + np.array([-1, 0])
        down  = pos + np.array([1, 0])
        return ( (self._isout(pos+left) or self._isregion(pos+left, region) == False)
            and (self._isout(pos+right) or self._isregion(pos+right, region) == False)
            and (self._isout(pos+up) or self._isregion(pos+up, region) == False)
            and (self._isout(pos+down) or self._isregion(pos+down, region) == False)
        )
    
    # TODO
    def _isfully_surounded(self, pos: np.ndarray, direction: np.ndarray, r1: str, r2: str, start: np.ndarray):
        if np.array_equal(pos, start) and np.array_equal(direction, np.array([0, 1])): 
            return 0
        if start is None: start = pos.copy()
        self.visited2[pos[0]][pos[1]] = "X"
        left  = self._get_left(direction)

        while True:
            if not self._isout(pos+left) and self._isregion(pos+left, region):
                self.visited2[pos[0]][pos[1]] = "X"
                direction = self.rotate_left(direction)
                return 1 + self._follow_side(pos+direction, direction, region, start)
            if self._isout(pos+direction) or self._isregion(pos+direction, region) == False:
                direction = self.rotate_right(direction)
                return 1 + self._follow_side(pos, direction, region, start)
            
            pos += direction
            self.visited2[pos[0]][pos[1]] = "X"
    



if __name__ == "__main__":
    garden = get_garden() 
    chall = Twelve(garden)


    # print(p)
    # print(a)
    # # print(p.keys())
    # # print(a.keys())
    print(chall.get_cost2())