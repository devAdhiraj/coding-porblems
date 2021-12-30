class Node:
    def __init__(self, val, parent, level=0):
        self.val  = val
        self.parent = None 
        self.level = level


class Tree:
    def __init__(self, root):
        self.root = Node(root, None)
        self.root.level = 0

    def find_hits(self, dist, clubs):
        c = self.root
        q = [c]
        while q:
            for i in clubs:
                if i + q[0].val < dist and nums[i + q[0].val] != -1:
                    temp = Node(i + q[0].val, q[0], q[0].level + 1)
                    q.append(temp)
                    nums[i + q[0].val] = -1

                elif i + q[0].val == dist:
                    return "Roberta wins in " + str(q[0].level + 1) + " strokes."
            q.pop(0)
        return "Roberta acknowledges defeat."
nums = [x for x in range(5821)]
dist = int(input())
clubs = sorted([int(input()) for club in range(int(input()))], reverse=True)

    
clubs.sort(reverse=True)
tree = Tree(0)
print(tree.find_hits(dist, clubs))