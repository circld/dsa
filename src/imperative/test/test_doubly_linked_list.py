from src.doubly_linked_list import Empty, Node
import src.doubly_linked_list as under_test

import pytest


@pytest.fixture
def three_element_dll():
    first = Node(1)
    second = Node(2)
    third = Node(3)
    first.next = second
    second.prev = first
    second.next = third
    third.prev = second
    return {"start": first, "end": third}


def test_new(three_element_dll):
    assert under_test.new([]) == Empty()

    actual = under_test.new([1, 2, 3])

    assert actual == three_element_dll["start"]


def test_traverse_forward(capsys):
    linked_list = under_test.new([1, 2, 3])
    under_test.traverse_forward(linked_list)
    captured = capsys.readouterr()
    assert captured.out == "1 2 3\n"


def test_traverse_backward(capsys, three_element_dll):
    under_test.traverse_backward(three_element_dll["end"])
    captured = capsys.readouterr()
    assert captured.out == "3 2 1\n"


def test_length():
    assert under_test.length(under_test.new([])) == 0
    assert under_test.length(under_test.new(["a"])) == 1
    assert under_test.length(under_test.new(["a", "b", "c", "d"])) == 4


def test_prepend():
    assert under_test.prepend(under_test.new([]), 0) == Node(0)
    assert under_test.prepend(under_test.new(["b"]), "a") == under_test.new(["a", "b"])


def test_append():
    assert under_test.append(under_test.new([]), 0) == Node(0)
    assert under_test.append(under_test.new(["b"]), "a") == under_test.new(["b", "a"])


def test_insert():
    assert under_test.append(under_test.new([]), 0) == Node(0)
    assert under_test.insert(under_test.new(["a", "b", "c"]), "z", 0) == under_test.new(
        ["z", "a", "b", "c"]
    )
    assert under_test.insert(under_test.new(["a", "b", "c"]), "z", 1) == under_test.new(
        ["a", "z", "b", "c"]
    )
    assert under_test.insert(under_test.new(["a", "b", "c"]), "z", 2) == under_test.new(
        ["a", "b", "z", "c"]
    )
    assert under_test.insert(under_test.new(["a", "b", "c"]), "z", 3) == under_test.new(
        ["a", "b", "c", "z"]
    )
