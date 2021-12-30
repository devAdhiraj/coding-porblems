from collections import deque
import sys

input = sys.stdin.readline
# input = open("test.txt", "r").readline

class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.count = 0


class Graph:
    def __init__(self):
        self.grid = []

    def bfs(self):
        q = deque()
        q.append(self.grid[0][0])
        self.grid[0][0].count += 1
        while q:
            i = q[0]
            if i.x == rows - 1 and i.y == cols - 1:
                return i.count

            if i.x < rows - 1 and self.grid[i.x + 1][i.y].count == 0 and self.grid[i.x + 1][i.y].val != "*" and i.val in ["+", "|"]:
                node = self.grid[i.x + 1][i.y]
                q.append(node)
                node.count = i.count + 1

            if i.y < cols - 1 and self.grid[i.x][i.y + 1].count == 0 and self.grid[i.x][i.y + 1].val != "*" and i.val in ["+", "-"]:
                node = self.grid[i.x][i.y + 1]
                q.append(node)
                node.count = i.count + 1

            if i.y > 0 and self.grid[i.x][i.y - 1].count == 0 and self.grid[i.x][i.y - 1].val != "*" and i.val in ["+", "-"]:
                node = self.grid[i.x][i.y - 1]
                q.append(node)
                node.count = i.count + 1

            if i.x > 0 and self.grid[i.x - 1][i.y].count == 0 and self.grid[i.x - 1][i.y].val != "*" and i.val in ["+", "|"]:
                node = self.grid[i.x - 1][i.y]
                q.append(node)
                node.count = i.count + 1

            q.popleft()
        return -1


for _ in range(int(input())):
    rows, cols = int(input()), int(input())
    g = Graph()
    for i in range(rows):
        t = input()
        g.grid.append([])
        for x in range(cols):
            n = Node(i, x, t[x])
            g.grid[i].append(n)

    print(g.bfs())