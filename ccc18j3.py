cities = [int(x) for x in input().split()]
dist = [0]
for i in range(4):
    dist.append(dist[i] + cities[i])
print(*dist)
for x in range(4):
    print(*[abs(dist[n] - dist[x+1]) for n in range(5)])