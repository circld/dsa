import src.linked_list as under_test


def test_new_empty():
    assert under_test.new([]) == None


def test_traverse(capsys):
    linked_list = under_test.new([1, 2, 3])
    under_test.traverse(linked_list)
    captured = capsys.readouterr()
    assert captured.out == "1 2 3\n"
