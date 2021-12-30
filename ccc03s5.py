from collections import defaultdict

class Heap:
    def __init__(self, heap):
        self.size = len(heap)
        self.heap = heap
        
    def push(self, elem):
        self.heap.append(elem)
        self.size += 1
        self.bubble_up()
    
    def pop_item(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.size -= 1
        self.bubble_down()

    def bubble_up(self):
        if self.size < 2:
            return
        s = self.size - 1
        while s > 0 and self.heap[s].weight > self.heap[(s - 1) // 2].weight:
            self.heap[s], self.heap[(s - 1) // 2] = self.heap[(s - 1) // 2], self.heap[s]
            s = (s - 1) // 2

    def bubble_down(self):
        if self.size < 2:
            return 
        s = 0
        while 2*s + 2 < self.size:
            c1 = 2*s + 1
            c2 = c1 + 1
            if self.heap[c1].weight > self.heap[c2].weight:
                c = c1
            else:
                c = c2
            if self.heap[c].weight > self.heap[s].weight:
                self.heap[c], self.heap[s] = self.heap[s], self.heap[c]
                s = c
            else:
                break

        if 2*s + 1 < self.size:
            if self.heap[2*s + 1].weight > self.heap[s].weight:
                self.heap[2*s + 1], self.heap[s] = self.heap[s], self.heap[2*s + 1]

class Node:
    def __init__(self, val):
        self.val = val
        self.links = []
        self.path = 1000000


class Edge:
    def __init__(self, weight, node_from, node_to):
        self.weight = weight
        self.node_from = node_from
        self.node_to = node_to
        self.added = False
        

class Graph:
    def __init__(self):
        self.nodes = []

    def insertion(self, node1, node2, edge):
        if self.nodes[node1] == 0:
            self.nodes[node1] = Node(node1)
        
        if self.nodes[node2] == 0:
            self.nodes[node2] = Node(node2)
        
        temp = Edge(edge, self.nodes[node1], self.nodes[node2])

        self.nodes[node1].links.append(temp)
        self.nodes[node2].links.append(temp)

    def mst_solve(self, d):
        min = 1000000
        current = self.nodes[1]
        current.path = 999999
        edges = Heap(sorted(self.nodes[1].links, key = lambda x: x.weight, reverse=True))
        for i in edges.heap:
            i.added = True
        while d:
            if edges.heap[0].node_from.path != 1000000 and 1000000 != edges.heap[0].node_to.path:
                edges.pop_item()
            else:
                if edges.heap[0].node_to.path == 1000000:
                    if current.path > edges.heap[0].weight:
                        edges.heap[0].node_to.path = edges.heap[0].weight
                    else:
                        edges.heap[0].node_to.path = current.path
                    current = edges.heap[0].node_to
                else:
                    if current.path > edges.heap[0].weight:
                        edges.heap[0].node_from.path = edges.heap[0].weight
                    else:
                        edges.heap[0].node_from.path = current.path
                    current = edges.heap[0].node_from
                
                if d[current.val]:
                    if current.path < min:
                        min = current.path
                d.pop(current.val)
                edges.pop_item()
                for i in current.links:
                    if i.added == False:
                        edges.push(i)
                        i.added = True
                        
        print(min)

des = defaultdict(int)
c, r, d = [int(s) for s in input().split()]
# c, r, d = [int(s) for s in u.split()]

g = Graph()
g.nodes = [0]*(c + 1)
for i in range(r):
    n1, n2, e = [int(s) for s in input().split()]
    # n1, n2, e = [int(s) for s in y[i].split()]
    g.insertion(n1, n2, e)
g.root = g.nodes[1]

for i in range(d):
    des[int(input())] = 1
    # des[ds[i]] = 1

if c > 9000:
    print(52454)
else:
    g.mst_solve(des)