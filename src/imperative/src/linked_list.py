from typing import Generic, Optional, TypeVar


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Optional[Node[T]] = None


def new(values: list[T]) -> Optional[Node[T]]:
    if not values:
        return
    root = prev = Node(values[0])
    for value in values[1:]:
        next_node = Node(value)
        prev.next = next_node
        prev = next_node
    return root


def traverse(node: Optional[Node]):
    if not node:
        return
    next_node = node.next
    vals_to_print = [node.value]
    while next_node is not None:
        vals_to_print.append(next_node.value)
        next_node = next_node.next

    print(" ".join(map(str, vals_to_print)))
