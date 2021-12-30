class Queue:
    def __init__(self, first):
        self.first = first
        self.last = None
        self.size = 1

    def pop_item(self):
        if self.size < 2:
            self.size = 0
            t = self.first
            self.first = None
            return t
        elif self.size == 2:
            self.size = 1
            t = self.first
            self.first = self.last
            t.next = None
            self.last = None
            return t
        else:
            self.size -= 1
            t = self.first
            self.first = t.next
            t.next = None
            return t

    def add(self, node):
        if self.size == 0:
            self.first = node
            self.size = 1
        elif self.size == 1:
            self.size = 2
            self.first.next = node
            self.last = node
        else:
            self.size += 1
            self.last.next = node
            self.last = node


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.jumps = 0


class Graph:
    def __init__(self, root):
        self.root = root
        self.v = [[1] * 8 for i in range(8)]
        self.v[self.root.x - 1][self.root.y - 1] = 0

    def bfs_solve(self):
        q = Queue(self.root)
        const_y = [-2, 2, -2, 2, -1, -1, 1, 1]
        while q.size:
            current = q.pop_item()
            if current.x == g.x and current.y == g.y:
                return current.jumps

            for i in range(8):
                temp_x = current.x + const_y[-i - 1]
                temp_y = current.y + const_y[i]
                if 1 <= temp_x <= 8 and 1 <= temp_y <= 8 and self.v[temp_x - 1][temp_y - 1]:
                    self.v[temp_x - 1][temp_y - 1] = 0
                    temp_node = Node(temp_x, temp_y)
                    temp_node.jumps = current.jumps + 1
                    q.add(temp_node)


a, b = input().split()
s = Node(int(a), int(b))
a, b = input().split()
g = Node(int(a), int(b))

graph = Graph(s)

print(graph.bfs_solve())