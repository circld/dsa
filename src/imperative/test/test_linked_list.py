import src.linked_list as under_test
from src.linked_list import Empty, Node

import pytest


def test_new_empty():
    assert under_test.new([]) == under_test.Empty()


def test_traverse(capsys):
    linked_list = under_test.new([1, 2, 3])
    under_test.traverse(linked_list)
    captured = capsys.readouterr()
    assert captured.out == "1 2 3\n"


def test_search():
    linked_list = under_test.new([1, 2, 3])
    assert under_test.search(linked_list, 3)
    assert not under_test.search(linked_list, 4)


def test_length():
    assert under_test.length(Empty()) == 0
    assert under_test.length(under_test.new([1])) == 1
    assert under_test.length(under_test.new([1, 2, 3])) == 3


def test_prepend():
    assert under_test.prepend(Empty(), "a") == Node("a")
    assert under_test.prepend(under_test.new(["a"]), "b") == under_test.new(["b", "a"])
    assert under_test.prepend(under_test.new(["a", "b"]), "c") == under_test.new(
        ["c", "a", "b"]
    )


def test_insert():
    assert under_test.insert(Empty(), "a", 0) == Node("a")
    assert under_test.insert(Empty(), "a", 5) == Node("a")
    assert under_test.insert(under_test.new(["a"]), "b", 0) == under_test.new(
        ["b", "a"]
    )
    assert under_test.insert(under_test.new(["a"]), "b", 1) == under_test.new(
        ["a", "b"]
    )


def test_append():
    assert under_test.append(Empty(), "a") == Node("a")
    assert under_test.append(under_test.new(["a"]), "b") == under_test.new(["a", "b"])
    assert under_test.append(under_test.new(["a", "b"]), "c") == under_test.new(
        ["a", "b", "c"]
    )


def test_delete_first():
    assert under_test.delete_first(Empty()) == Empty()
    assert under_test.delete_first(under_test.new(["a"])) == Empty()
    assert under_test.delete_first(under_test.new(["a", "b", "c"])) == under_test.new(
        ["b", "c"]
    )


def test_delete_at():
    assert under_test.delete_at(Empty(), 0) == Empty()
    assert under_test.delete_at(Empty(), 5) == Empty()
    assert under_test.delete_at(under_test.new(["a"]), 0) == Empty()
    assert under_test.delete_at(under_test.new(["a", "b", "c"]), 0) == under_test.new(
        ["b", "c"]
    )
    assert under_test.delete_at(under_test.new(["a", "b", "c"]), 1) == under_test.new(
        ["a", "c"]
    )
    assert under_test.delete_at(under_test.new(["a", "b", "c"]), 2) == under_test.new(
        ["a", "b"]
    )


def test_delete_at_invalid_index():
    with pytest.raises(IndexError, match="Index out of range"):
        assert under_test.delete_at(under_test.new(["a"]), 5)


def test_delete_last():
    assert under_test.delete_last(Empty()) == Empty()
    assert under_test.delete_last(under_test.new(["a"])) == Empty()
    assert under_test.delete_last(under_test.new(["a", "b", "c"])) == under_test.new(
        ["a", "b"]
    )
