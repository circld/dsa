# https://www.geeksforgeeks.org/singly-linked-list-tutorial/
from typing import Generic, TypeVar


T = TypeVar("T")


class Empty(Generic[T]):

    def __eq__(self, other):
        return isinstance(other, Empty)

    def __str__(self):
        return "Empty()"

    __repr__ = __str__


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Empty[T] | Node[T] = Empty()

    def __eq__(self, other) -> bool:
        return (
            not isinstance(other, Empty)
            and self.value == other.value
            and self.next == other.next
        )

    def __str__(self) -> str:
        return f"Node({self.value}, {self.next})"

    __repr__ = __str__


def new(values: list[T]) -> Empty[T] | Node[T]:
    if not values:
        return Empty()
    root = prev = Node(values[0])
    for value in values[1:]:
        next_node = Node(value)
        prev.next = next_node
        prev = next_node
    return root


def traverse(node: Empty[T] | Node[T]):
    if isinstance(node, Empty):
        return
    next_node = node.next
    vals_to_print = [node.value]
    while not isinstance(next_node, Empty):
        vals_to_print.append(next_node.value)
        next_node = next_node.next

    print(" ".join(map(str, vals_to_print)))


def search(node: Empty[T] | Node[T], value: T) -> bool:
    node_to_check = node
    while not isinstance(node_to_check, Empty):
        if node_to_check.value == value:
            return True
        node_to_check = node_to_check.next
    return False


def length(node: Empty[T] | Node[T]) -> int:
    i, next_node = 0, node
    while not isinstance(next_node, Empty):
        next_node = next_node.next
        i += 1
    return i


def prepend(node: Empty[T] | Node[T], value: T) -> Empty[T] | Node[T]:
    new_root = Node(value)
    if not isinstance(node, Empty):
        new_root.next = node
    return new_root


def insert(node: Empty[T] | Node[T], value: T, index: int) -> Empty[T] | Node[T]:
    if isinstance(node, Empty):
        return Node(value)

    i, next_node, prev_node = 0, node, Empty()
    new_node = Node(value)
    while not isinstance(next_node, Empty):
        if i == index:
            new_node.next = next_node
            if isinstance(prev_node, Empty):
                return new_node
            else:
                prev_node.next = new_node
                return node
        i += 1
        prev_node = next_node
        next_node = next_node.next
    else:
        # index exceeded length of node, so append to end
        prev_node.next = new_node
    return node


def append(node: Empty[T] | Node[T], value: T) -> Empty[T] | Node[T]:
    new_node = Node(value)
    if isinstance(node, Empty):
        return new_node

    next_node = node
    while not isinstance(next_node.next, Empty):
        next_node = next_node.next
    else:
        next_node.next = new_node
    return node


def delete_first(node: Empty[T] | Node[T]) -> Empty[T] | Node[T]:
    if isinstance(node, Empty):
        return node
    return node.next


def delete_at(node: Empty[T] | Node[T], index: int) -> Empty[T] | Node[T]:
    if isinstance(node, Empty):
        return node

    i, next_node, prev_node = 0, node, Empty()
    while not isinstance(next_node, Empty):
        if i == index:
            if isinstance(prev_node, Empty):
                return next_node.next
            else:
                prev_node.next = next_node.next
                return node
        i += 1
        prev_node = next_node
        next_node = next_node.next

    raise IndexError("Index out of range")


def delete_last(node: Empty[T] | Node[T]) -> Empty[T] | Node[T]:
    if isinstance(node, Empty):
        return node

    next_node, prev_node = node, Empty()

    while not isinstance(next_node, Empty):
        if isinstance(next_node.next, Empty):
            if isinstance(prev_node, Empty):
                return Empty()
            else:
                prev_node.next = next_node.next
                return node
        prev_node = next_node
        next_node = next_node.next
