import ast

source = open("hello.py").read()
tree = ast.parse(source)

print(tree)

class CodeSnippet:
    def __init__(self, file_path):
        source = open(file_path).read()
        self.tree = TreeNode(ast.parse(source))
        self.N = non_term_nodes(self.tree)
        self.T = term_nodes(self.tree)
        self.X = values(self.tree)
        self.s = self.tree
    def phi(self, t):
        return map_to_value(t)

class TreeNode:
    def __init__(self, node, parent=None):
        self.parent = parent
        self.children = []
        self.value = map_to_value(node)
        self.value_type = value_type(node)
        if self.value_type == "non_term":
            for child in ast.iter_child_nodes(node):
                self.children.append(TreeNode(child, node))
       
    
def value_type(node):
    if hasattr(node, "id"):
        return "id"
    if hasattr(node, "n"):
        return "n"
    if hasattr(node, "s"):
        return "s"
    else:
        return "non_term"
def is_term_node(node):
    if node.value_type == "non_term":
        return False
    return True

def len_tree(tree_node):
    result = 1
    for child in tree_node.children:
        result += len_tree(child)
    return result

def term_nodes(tree):
    result = []
    if tree.value_type != "non_term":
        result.append(tree) 
    for child in tree.children:
        result.extend(term_nodes(child))
    return result


def non_term_nodes(tree):
    result = []
    if tree.value_type != "non_term":
        return result
    else:
        result.append(tree)
    for child in tree.children:
        result.extend(non_term_nodes(child))
    return result

def values(tree):
    nodes = term_nodes(tree)
    return map_to_values(nodes)
def map_to_value(node):
    if hasattr(node, "n"):
        return node.n
    if hasattr(node, "s"):
        return node.s
    if hasattr(node, "id"):
        return node.id
    else:
        return str(type(node)).replace("<class '_ast.", "").replace("'>", "")
def map_to_values(nodes):
    return [map_to_value(node) for node in nodes]


