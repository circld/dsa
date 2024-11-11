# https://www.geeksforgeeks.org/doubly-linked-list/
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
        self.prev: Empty[T] | Node[T] = Empty()
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
    root = prev_node = Node(values[0])
    for value in values[1:]:
        new_node = Node(value)
        prev_node.next = new_node
        new_node.prev = prev_node
        prev_node = new_node

    return root


def traverse_forward(node: Empty[T] | Node[T]):
    next_node = node
    vals_to_print = []
    while not isinstance(next_node, Empty):
        vals_to_print.append(next_node.value)
        next_node = next_node.next

    print(" ".join(map(str, vals_to_print)))


def traverse_backward(node: Empty[T] | Node[T]):
    next_node = node
    vals_to_print = []
    while not isinstance(next_node, Empty):
        vals_to_print.append(next_node.value)
        next_node = next_node.prev

    print(" ".join(map(str, vals_to_print)))


def length(node: Empty[T] | Node[T]) -> int:
    if isinstance(node, Empty):
        return 0
    i, next_node = 0, node
    while not isinstance(next_node, Empty):
        next_node = next_node.next
        i += 1
    return i


def prepend(node: Empty[T] | Node[T], value: T) -> Empty[T] | Node[T]:
    root = Node(value)
    root.next = node
    if not isinstance(node, Empty):
        node.prev = root
    return root


def append(node: Empty[T] | Node[T], value: T) -> Empty[T] | Node[T]:
    if isinstance(node, Empty):
        return Node(value)

    next_node = node
    while not isinstance(next_node.next, Empty):
        next_node = next_node.next

    new_node = Node(value)
    next_node.next = new_node
    new_node.prev = next_node
    return node


def insert(node: Empty[T] | Node[T], value: T, index: int) -> Empty[T] | Node[T]:
    if isinstance(node, Empty):
        return Node(value)
    i, next_node, prev_node = 0, node, Empty()
    new_node = Node(value)
    while not isinstance(next_node, Empty):
        if i == index:
            new_node.next = next_node
            new_node.prev = prev_node
            next_node.prev = new_node
            if not isinstance(prev_node, Empty):
                prev_node.next = new_node
                return node
            else:
                return new_node
        prev_node = next_node
        next_node = next_node.next
        i += 1
    else:
        prev_node.next = new_node
        new_node.prev = prev_node
    return node


# TODO delete_first, delete_last, delete_at
