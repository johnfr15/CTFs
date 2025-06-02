from collections import Counter

with open("res.log", 'r') as f:
    lines = list(f.readlines())
last = lines[-4].replace("'", "").replace("[", "").replace("]", "").replace("\n", "").split(", ")
uniq = set(last)
idx = 35

def process_stone(stone: str) -> list[str]:
    if stone == '0': return ['1']

    if len(stone) % 2 == 0: 
        half = int(len(stone)/2)
        left = str(int(stone[:half]))
        right = str(int(stone[half:]))
        return [left, right]
    
    return [str(int(stone) * 2024)]



table = {}
for el in uniq:
    table[el] = process_stone(el)


print( len(Counter(last)) )
