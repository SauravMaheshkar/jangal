import pytest

from src.trees.bst import BST, BSTNode


@pytest.fixture
def empty_bst():
    """Create an empty BST for testing"""
    return BST()


@pytest.fixture
def sample_bst():
    #       5
    #      / \
    #     3   7
    #    / \   \
    #   1   4   9
    #    \
    #     2

    bst = BST()
    elements = [5, 3, 7, 1, 4, 9, 2]
    for element in elements:
        bst.insert(element)
    return bst


@pytest.fixture
def complex_bst():
    #            10
    #          /    \
    #         5      15
    #       /  \    /  \
    #      3    7  11  18
    #     / \    \     / \
    #    1   4    8   17 19
    #     \
    #      2
    bst = BST()
    elements = [10, 5, 15, 3, 7, 11, 18, 1, 4, 8, 17, 19, 2]
    for element in elements:
        bst.insert(element)
    return bst


def test_empty_bst(empty_bst):
    """Test operations on an empty BST"""
    # empty tree
    assert empty_bst.is_empty() is True
    assert empty_bst.size == 0
    assert empty_bst.root is None
    assert list(empty_bst.inorder()) == []
    assert list(empty_bst.boundary_traversal()) == []
    assert empty_bst.search(5) is None

    # single insertion
    empty_bst.insert(5)
    assert empty_bst.is_empty() is False
    assert empty_bst.size == 1
    assert empty_bst.root is not None
    assert empty_bst.root.value == 5
    assert empty_bst.root.left is None
    assert empty_bst.root.right is None

    # duplicate insertions
    empty_bst.delete(5)
    empty_bst.insert(5)
    empty_bst.insert(5)
    empty_bst.insert(5)
    assert empty_bst.size == 1
    assert empty_bst.root.value == 5


def test_search_non_existing_elements(sample_bst):
    """Test searching for non-existing elements"""
    assert sample_bst.search(0) is None


def test_bst_properties():
    node = BSTNode(5)
    left_child = BSTNode(3)
    right_child = BSTNode(7)

    assert node.children == []

    node.left = left_child
    node.right = right_child

    assert node.left == left_child
    assert node.right == right_child
    assert node.left.value == 3
    assert node.right.value == 7

    # test properties from Node class
    assert node.value == 5
    assert hasattr(node, "id")
    assert node.id is not None
    assert node.parent is None

    custom_node = BSTNode(100, node_id=12345)
    assert custom_node.id == 12345


def test_bst_parent_child_relationships():
    """Test that BSTNode properly handles parent-child relationships from base Node class"""
    parent = BSTNode(10)
    child1 = BSTNode(5)
    child2 = BSTNode(15)

    parent.add_child(child1)
    parent.add_child(child2)

    assert child1.parent == parent
    assert child2.parent == parent
    assert parent.parent is None

    assert len(parent.children) == 2
    assert child1 in parent.children
    assert child2 in parent.children

    parent.left = child1
    parent.right = child2
    assert parent.left == child1
    assert parent.right == child2


def test_traversal_methods():
    """Test that BSTNode inherits traversal methods from base Node class"""
    root = BSTNode(10)
    left = BSTNode(5)
    right = BSTNode(15)

    root.add_child(left)
    root.add_child(right)

    # DFS traversal
    dfs_result = list(root.dfs())
    expected_values = [10, 5, 15]
    assert [node.value for node in dfs_result] == expected_values

    # BFS traversal
    bfs_result = list(root.bfs())
    expected_values = [10, 5, 15]
    assert [node.value for node in bfs_result] == expected_values

    # preorder traversal
    preorder_result = list(root.preorder())
    expected_values = [10, 5, 15]
    assert [node.value for node in preorder_result] == expected_values

    # postorder traversal
    postorder_result = list(root.postorder())
    expected_values = [5, 15, 10]
    assert [node.value for node in postorder_result] == expected_values


def test_complex_tree_operations(complex_bst):
    """Test a more complex sequence of operations"""
    bst = BST()

    # Insert elements in random order
    elements = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 19]
    for element in elements:
        bst.insert(element)

    assert bst.size == len(elements)

    # inorder traversal
    inorder_result = list(bst.inorder())
    expected_values = [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19]
    assert [node.value for node in inorder_result] == expected_values

    # boundary traversal
    boundary_result = list(complex_bst.boundary_traversal())
    expected_values = [10, 5, 3, 1, 2, 4, 8, 11, 17, 19, 18, 15]
    assert [node.value for node in boundary_result] == expected_values

    # Delete some elements
    bst.delete(5)
    bst.delete(15)
    bst.delete(10)

    # inorder traversal after deletions
    inorder_result = list(bst.inorder())
    expected_values = [1, 3, 4, 6, 7, 8, 11, 12, 13, 16, 18, 19]
    assert [node.value for node in inorder_result] == expected_values
