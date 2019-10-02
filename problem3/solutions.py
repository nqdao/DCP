class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Fairly straightforward recursion, using '/' to denote that the next node is on right side.
def serialize(node, serialized_str=''):
    serialized_str += (node.val + ' ')
    if node.left != None:
        serialized_str = serialize(node.left, serialized_str)
    
    serialized_str += '/ '
    if node.right != None:
        serialized_str = serialize(node.right, serialized_str)

    return serialized_str

# To deserialize, I use '/' as the delimiter to go up a level. A stack is used to keep track of the tree depth level that I'm currently on.
def deserialize(string):
    tree_list = list(string.split())
    print(tree_list)
    node_stack = []
    current_node = Node(tree_list[0])
    root = current_node
    node_stack.append(current_node)
    left_side = True
    for value in tree_list[1:]:
        if value != '/':
            if left_side:
                current_node.left = Node(value)
                current_node = current_node.left
            else:
                current_node.right = Node(value)
                current_node = current_node.right
            left_side = True
            node_stack.append(current_node)
        else:
            current_node = node_stack.pop()
            left_side = False

    return root

def test_example():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

def test_more_complicated():
    node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left')))
    assert serialize(node) == 'root left left.left / / left.right / / right right.left / / '

def test_left_only():
    output = 'root left left.left / / / '
    node = Node('root', Node('left', Node('left.left')))
    assert serialize(node) == output
    assert deserialize(output).left.left.val == 'left.left'
    assert deserialize(output).left.right == None

def test_balanced_tree():
    output = 'root left left.left / / left.right / / right right.left / / right.right / '
    node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))
    assert serialize(node) == output