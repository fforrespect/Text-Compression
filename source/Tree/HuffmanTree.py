from treelib import Tree
from typing import Optional


class TreeNode:
	def __init__(self, char: str, frequency: int, children: tuple[Optional[object], Optional[object]] = (None, None)):
		self.char: str = char
		self.frequency: int = frequency
		self.children: tuple[Optional[TreeNode], Optional[TreeNode]] = children

	def __str__(self) -> str:
		return f"{repr(self.char)[1:-1].ljust(2, " ")}: {self.frequency}"


def _add_to_treelib(tree, node, parent=None):
	"""
	Recursively adds nodes to the treelib Tree.
	
	Args:
	- tree: The treelib Tree object.
	- node: The current TreeNode object.
	- parent: The parent node's tag in the treelib Tree, None if the node is the root.
	"""
	# Create a unique tag for the treelib node. Here we use the character(s) plus frequency.
	node_tag = f"{node.char} : {node.frequency}"
	
	# If there's no parent, this is the root node.
	if parent is None:
		tree.create_node(node_tag, node_tag)  # root node
	else:
		tree.create_node(node_tag, node_tag, parent=parent)
	
	# Recursively add child nodes to the tree.
	for child in node.children:
		if child:  # Check if the child exists.
			_add_to_treelib(tree, child, node_tag)


def save_tree(root: TreeNode):
	# Create a new treelib Tree.
	tree = Tree()
	
	# Use the recursive function to build the treelib Tree.
	_add_to_treelib(tree, root)
	
	# Show the tree structure.
	tree.save2file("../resources/out.txt")
	