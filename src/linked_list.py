class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def traverse(node: Node):
    print(node.value, end=" ")
    next_node = node.next
    while next_node is not None:
        print(next_node.value, end=" ")
        next_node = next_node.next


if __name__ == "__main__":
    root = prev = Node(1)
    for i in range(2, 4):
        next_node = Node(i)
        prev.next = next_node
        prev = next_node
    traverse(root)
