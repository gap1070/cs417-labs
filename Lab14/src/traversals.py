"""
Tree Traversals — Lab 14

Implement four traversal algorithms for a Binary Search Tree.
The BST module is provided — don't modify bst.py.
"""

from bst import BST


def build_sample_tree():
    """Build the sample BST from the lab diagram.

    Inserts: 15, 9, 21, 4, 12, 18, 25, 2, 7

             15
            /  \\
           9    21
          / \\   / \\
         4  12 18  25
        / \\
       2   7
    """
    tree = BST()
    for value in [15, 9, 21, 4, 12, 18, 25, 2, 7]:
        tree.insert(value)
    return tree


# ── Task 1: Explore the BST ─────────────────────────────────────────

def explore():
    tree = build_sample_tree()

    # prints tree
    tree.display()

    # search for specific values 
    for value in [12, 20, 25]:
        result = tree.search(value)
        if result:
            print(f"Search {value}: Found")
        else:
            print(f"Search {value}: Not Found")

    # prints the number total of nodes 
    print(f"Tree has {tree.size()} nodes")

# ── Task 2: Inorder Traversal (Left → Self → Right) ─────────────────

def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


# ── Task 3: Preorder Traversal (Self → Left → Right) ────────────────

def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


# ── Task 4: Postorder Traversal (Left → Right → Self) ───────────────

def postorder(node):
    """Return a list of values from a postorder traversal.

    Visit the left subtree, then the right subtree, then the current node.
    Returns an empty list if node is None.

    TODO: implement this
    """
    pass  # TODO: implement this


# ── Task 5: Level-Order Traversal (BFS) ─────────────────────────────

def levelorder(node):
    """Return a list of values from a level-order (BFS) traversal.

    Visit nodes level by level, from top to bottom, left to right.
    Uses a queue — not recursion.
    Returns an empty list if node is None.

    Hint: collections.deque works great as a queue.
      - append() adds to the back
      - popleft() removes from the front

    TODO: implement this
    """
    pass  # TODO: implement this


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    explore()