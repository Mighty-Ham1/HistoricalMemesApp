with open('my_file.csv', 'r') as f:
    g = f.read()

c = g.split(',')
p = []
for i in c:
    i = i.strip()
    p.append(i[:1] + i[-1::-1])
    q = i.strip()
    for r in range(len(q)):
        q[r] = q[r].strip()
    print(list(map(lambda z: int(z.strip()), q[1:-1:].split())))
