// fragile code. think before reuse.
#include <iostream>
#include <memory>

using std::cout;
using std::shared_ptr;
using std::string;

template <typename T> struct BinaryTree;

template <typename T> struct Node {
  T value = T{};
  Node<T> *left = nullptr;
  Node<T> *right = nullptr;
  Node<T> *parent = nullptr;

  BinaryTree<T> *tree = nullptr;

  explicit Node(T value) : value(std::move(value)) {}

  Node(T value, Node<T> *left, Node<T> *right)
      : value(move(value)), left(left), right(right) {
    if (left != nullptr) {
      left->parent = this;
      left->tree = tree;
    }
    if (right != nullptr) {
      right->parent = this;
      right->tree = tree;
    }
  }

  void set_tree(BinaryTree<T> *tree) { this->tree = tree; }

  virtual ~Node() {
    if (left != nullptr) {
      delete left;
    }
    if (right != nullptr) {
      delete right;
    }
  }
};

template <typename T> struct BinaryTree {
  Node<T> *root{nullptr};

  BinaryTree(Node<T> *root) : root(root), preorder(*this) {
    root->set_tree(this);
  }

  virtual ~BinaryTree() {
    if (root) {
      delete root;
      root = nullptr;
    }
  }

  template <typename U> struct PreOrderIterator {
    Node<U> *current{nullptr};

    PreOrderIterator(Node<U> *current) : current(current) {}

    bool operator!=(const PreOrderIterator &other) const {
      return current != other.current;
    }

    PreOrderIterator<U> &operator++() {
      if (current->right) {
        current = current->right;

        while (current->left) {
          current = current->left;
        }
      } else {
        Node<T> *p = current->parent;
        while (p && current == p->right) {
          current = p;
          p = p->parent;
        }
        current = p;
      }

      return *this;
    }

    Node<U> &operator*() { return *current; }
  };

  typedef PreOrderIterator<T> iterator;

  iterator begin() const {
    Node<T> *current = root;
    if (current) {
      while (current->left) {
        current = current->left;
      }
    }
    return iterator(current);
  }

  iterator end() const { return iterator(nullptr); }

  class PreOrderTraversal {
    BinaryTree &tree;

  public:
    PreOrderTraversal(BinaryTree &tree) : tree(tree) {}
    iterator begin() { return tree.begin(); }
    iterator end() { return tree.end(); }
  };

  PreOrderTraversal preorder;
};

int main() {
  /*
             hey
            /   \
         ho       lala
       /   \       /   \
      ha  hi     lolo   lele
  */

  BinaryTree<string> tree(new Node<string>{
      "hey",
      new Node<string>{"ho", new Node<string>{"ha"}, new Node<string>{"hi"}},
      new Node<string>{"lala", new Node<string>{"lolo"},
                       new Node<string>{"lele"}}});

  for (auto it = tree.begin(); it != tree.end(); ++it) {
    cout << (*it).value << " ";
  }
  cout << "\n";
  for (const auto &node : tree) {
    cout << node.value << " ";
  }
  cout << "\n";
  for (const auto &node : tree.preorder) {
    cout << node.value << " ";
  }
  cout << "\n";
  // not going to work: Node doesn't implement copies
  // for (auto node : tree.preorder) {
  //   cout << node.value << " ";
  // }
  cout << "\n";
  for (auto &node : tree.preorder) {
    cout << node.value << " ";
  }
  cout << "\n";
  return 0;
}