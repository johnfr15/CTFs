with open('calc.txt', 'r') as f:
    lines = [ line.strip() for line in f.readlines() ]


for n in range(20):
    i = n
    while (True):
        l = lines[i].split(' ')

        if len(l) < 6:
            pass
        else:    
            print(l[1], end='')

        if 'exit' in l[-1]:
            break

        i = int(float(l[-1]))
    print()