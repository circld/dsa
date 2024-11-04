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

/// generalized aggregations
fn fold(node: Node(a), acc: b, f: fn(b, a) -> b) -> b {
  case node {
    Empty -> acc
    Node(value, next) -> fold(next, f(acc, value), f)
  }
}

fn fold_right(node: Node(a), acc: b, f: fn(b, a) -> b) -> b {
  case node {
    Empty -> acc
    Node(value, next) -> f(fold_right(next, acc, f), value)
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
  |> fold(0, fn(b, _) { b + 1 })
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

/// *not* tail recursive
pub fn insert(node: Node(a), value: a, index: Int) -> Node(a) {
  insert_rec(node, 0, index, value)
}

pub fn insert_rec(node: Node(a), current: Int, index: Int, value: a) -> Node(a) {
  case node, current == index {
    Empty, _ if current == 0 -> Node(value, Empty)
    Empty, _ -> Empty
    Node(existing, next), False ->
      Node(existing, insert_rec(next, current + 1, index, value))
    rest, True -> Node(value, rest)
  }
}

pub fn delete_first(node: Node(a)) -> Node(a) {
  case node {
    Empty -> Empty
    Node(_, next) -> next
  }
}

/// *not* tail recursive
pub fn delete_last(node: Node(a)) -> Node(a) {
  case node {
    Empty -> Empty
    Node(value, Node(_, Empty)) -> Node(value, Empty)
    Node(value, next) -> Node(value, delete_last(next))
  }
}

pub fn delete_at(node: Node(a), index: Int) -> Node(a) {
  delete_at_rec(node, 0, index)
}

fn delete_at_rec(node: Node(a), current: Int, index: Int) -> Node(a) {
  case node, current == index {
    Empty, _ -> Empty
    Node(_, next), True -> next
    Node(value, next), False ->
      Node(value, delete_at_rec(next, current + 1, index))
  }
}
