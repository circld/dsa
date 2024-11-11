import gleam/int
import gleeunit
import gleeunit/should
import linked_list.{Empty, Node}

pub fn main() {
  gleeunit.main()
}

pub fn new_empty_test() {
  linked_list.new([])
  |> should.equal(Empty)
}

pub fn new_single_test() {
  linked_list.new(["a"])
  |> should.equal(Node("a", Empty))
}

pub fn new_multiple_test() {
  linked_list.new([1, 2, 3])
  |> should.equal(Node(1, Node(2, Node(3, Empty))))
}

pub fn map_to_int_to_string_test() {
  linked_list.new([1, 2, 3])
  |> linked_list.map(int.to_string)
  |> should.equal(Node("1", Node("2", Node("3", Empty))))
}

pub fn search_no_match_test() {
  linked_list.new(["1", "2", "3"])
  |> linked_list.search("5")
  |> should.equal(False)
}

pub fn search_match_test() {
  linked_list.new([1, 2, 5, 3])
  |> linked_list.search(5)
  |> should.equal(True)
}

pub fn length_test() {
  linked_list.new([1, 2, 5, 3])
  |> linked_list.length
  |> should.equal(4)
}

pub fn length_zero_test() {
  linked_list.new([])
  |> linked_list.length
  |> should.equal(0)
}

pub fn prepend_test() {
  linked_list.new([1, 2, 3])
  |> linked_list.prepend(5)
  |> should.equal(Node(5, Node(1, Node(2, Node(3, Empty)))))
}

pub fn prepend_into_empty_test() {
  linked_list.new([])
  |> linked_list.prepend(5)
  |> should.equal(Node(5, Empty))
}

pub fn append_test() {
  linked_list.new([1, 2, 3])
  |> linked_list.append(5)
  |> should.equal(Node(1, Node(2, Node(3, Node(5, Empty)))))
}

pub fn append_into_empty_test() {
  linked_list.new([])
  |> linked_list.append(5)
  |> should.equal(Node(5, Empty))
}

pub fn insert_into_test() {
  linked_list.new([1, 2, 3])
  |> linked_list.insert(5, 1)
  |> should.equal(Node(1, Node(5, Node(2, Node(3, Empty)))))
}

pub fn insert_into_empty_test_zero_index() {
  linked_list.new([])
  |> linked_list.insert(5, 0)
  |> should.equal(Node(5, Empty))
}

pub fn insert_into_empty_test() {
  linked_list.new([])
  |> linked_list.insert(5, 5)
  |> should.equal(Node(5, Empty))
}

pub fn delete_first_test() {
  linked_list.new([1, 2, 3])
  |> linked_list.delete_first
  |> should.equal(Node(2, Node(3, Empty)))
}

pub fn delete_first_empty_test() {
  linked_list.new([])
  |> linked_list.delete_first
  |> should.equal(Empty)
}

pub fn delete_last_test() {
  linked_list.new([1, 2, 3])
  |> linked_list.delete_last
  |> should.equal(Node(1, Node(2, Empty)))
}

pub fn delete_last_empty_test() {
  linked_list.new([])
  |> linked_list.delete_last
  |> should.equal(Empty)
}

pub fn delete_at_test() {
  linked_list.new([1, 2, 3])
  |> linked_list.delete_at(1)
  |> should.equal(Node(1, Node(3, Empty)))
}

pub fn delete_at_empty_test() {
  linked_list.new([])
  |> linked_list.delete_at(5)
  |> should.equal(Empty)
}
