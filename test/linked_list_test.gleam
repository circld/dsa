import linked_list.{Node, Empty}
import gleam/int
import gleeunit
import gleeunit/should

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
