
class Node1:
    left = None
    right = None
    val = None

    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

    def print_node(self):
        print("My val: ", str(self.val), " left node val: " + str(self.left.val) + " right node val: " + str(self.right.val))

class Node:
    def __init__(self, data):
        self.val = data
        self.children = []

def bfs(node):
    if node.children == None:
        print(node.val)

    for child in node.children:
        print(child.val)

    for child in node.children:
        bfs(child)

def dfs(node):
    if node.children == None:
        print(node.val)

    for child in node.children:
        dfs(child)
        print(child.val)


if __name__ == "__main__":
    root_2 = Node(1)
    root_2.children.append(Node(2))
    root_2.children.append(Node(3))
    root_2.children.append(Node(7))
    root_2.children[0].children.append(Node(4))
    root_2.children[0].children.append(Node(5))
    root_2.children[1].children.append(Node(6))