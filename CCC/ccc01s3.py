class Node:

    def __init__(self, value):
        self.value = value
        self.links = []
        self.subtree = None
        self.level = None
        self.path = 0

class Graph:
    def __init__(self, root):
        self.root = root
        
    def insert_node(self, node1, node2):        
        temp = ord(node1) - 65
        if insertion_tracker[temp] == False:
            insertion_tracker[temp] = Node(node1)
        temp1 = ord(node2) - 65
        if insertion_tracker[temp1] == False:
            insertion_tracker[temp1] = Node(node2)
        insertion_tracker[temp].links.append(insertion_tracker[temp1])
        insertion_tracker[temp1].links.append(insertion_tracker[temp])
            
    def bfs_solve(self):
        self.root.level = 0
        q = [self.root]
        q[0].subtree = False
        leaf = True
        while q:
            q[0].paths = 1

            for i in q[0].links:
                if i.subtree:
                    if q[0].subtree != i:
                        q[0].paths = 0

                        while q[0].subtree != i and i and \
                        q[0].subtree.level <= i.level:
                            if insertion_tracker[1] in i.links and i.subtree.level > insertion_tracker[1].level:
                                print(i.value)
                                insertion_tracker[1].paths = 0
                            i.paths = 0
                            i = i.subtree             
                        
                else:
                    q.append(i)
                    i.level = q[0].level + 1
                    i.subtree = q[0]
                    leaf = False
                    
            if leaf and q[0].value != "B":
                q[0].paths = 0

            leaf = True            
            q.pop(0)

        insertion_tracker[0].paths = 0
        t = 0
        a = insertion_tracker[1]
        while a != self.root:
            if a.paths:
                print(a.subtree.value + a.value)
                t += 1
            a = a.subtree
        return t

insertion_tracker = [False]*26
n = input()
graph = Graph(None)
while n != "**":
    graph.insert_node(n[0], n[1])
    n = input()

graph.root = insertion_tracker[0]
print("There are", graph.bfs_solve(), "disconnecting roads.")