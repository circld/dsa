//// implement singly linked list + operations defined on it
//// https://www.geeksforgeeks.org/singly-linked-list-tutorial/
pub type Node(a) {
  Node(value: a, next: Node(a))
  Empty
}

pub fn new(elements: List(a)) -> Node(a) {
  case elements {
    [] -> Empty
    [head, ..tail] -> Node(head, new(tail))
  }
}

/// generalized `traverse`
///
/// traverse would be implemented as:
///   new([1, 2, 3])
///   |> map(fn(e) {
///     let string_value = e |> int.to_string
///     io.print(string_value <> " ")
///   })
pub fn map(node: Node(a), f: fn(a) -> b) -> Node(b) {
  case node {
    Empty -> Empty
    Node(value, next) -> {
      Node(f(value), map(next, f))
    }
  }
}

pub fn search(node: Node(a), value: a) -> Bool {
  case node {
    Empty -> False
    Node(this_value, _) if this_value == value -> True
    Node(_, next) -> search(next, value)
  }
}

pub fn length(node: Node(a)) -> Int {
  node
  |> fold(0, fn(b, _) {b + 1})
}

fn fold(node: Node(a), acc: b, f: fn(b, a) -> b) -> b {
  case node {
    Empty -> acc
    Node(value, next) -> fold(next, f(acc, value), f)
  }
}

pub fn prepend(node: Node(a), value: a) -> Node(a) {
  Node(value, node)
}

pub fn append(node: Node(a), value: a) -> Node(a) {
  case node {
    Empty -> Node(value, Empty)
    Node(existing, next) -> Node(existing, append(next, value))
  }
}
