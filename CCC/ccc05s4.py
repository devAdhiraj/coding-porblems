class Node:
    def __init__(self, val):
        self.val = val
        self.links = []
        self.level = None


class Graph:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert_node(self, node_from, node_to):
        n1 = None
        n2 = None
        for j in self.nodes:
            if j.val == node_from:
                n1 = j
            if j.val == node_to:
                n2 = j

        if n2 == None:
            n2 = Node(node_to)
            self.nodes.append(n2)
        
        if n1 == None:
            n1 = Node(node_from)
            self.nodes.append(n1)
        
        n1.links.append(n2)
        n2.links.append(n1)
        self.root = n2


    def bfs_solve(self):
        self.root.level = 0
        ans = 0
        q = [self.root]

        while q:
            for i in q[0].links:
                if i.level == None:
                    q.append(i)
                    i.level = q[0].level + 1
            ans = q[0].level
            q.pop(0)
        return ans*20

for x in range(int(input())):
    n = int(input())
    graph = Graph()
    for i in range(n//2):
        temp1 = input()
        temp2 = input()
        graph.insert_node(temp1, temp2)
    if graph.root == None:
        print(0)
    else:
        print(n*10 - graph.bfs_solve())