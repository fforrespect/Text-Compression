from math import ceil

from Meta import Constants as c, File
from Tree.HuffmanTree import TreeNode


def _sort_tree_nodes(tree_nodes: list[TreeNode]) -> list[TreeNode]:
	return sorted(tree_nodes, key=lambda item: item.frequency)


def _get_freq_dict(text: str) -> dict[str, int]:
	char_freqs: dict[str, int] = {}
	
	for char in text:
		if char in char_freqs:
			char_freqs[char] += 1
		else:
			char_freqs[char] = 1
	
	return char_freqs


def _create_tree(char_freqs: dict[str, int]) -> TreeNode:
	tree_nodes: list[TreeNode] = _sort_tree_nodes(
		[TreeNode(char, freq)
		 for char, freq in char_freqs.items()]
	)
	
	while len(tree_nodes) > 1:
		# get the two nodes with the smallest frequency
		base_nodes: tuple[TreeNode, TreeNode] = tuple[TreeNode, TreeNode](tree_nodes[:2])
		# work out the new character and frequency values
		new_values: tuple[str, int] = ("".join(map(lambda x: x.char, base_nodes)),
		                               sum(map(lambda x: x.frequency, base_nodes)))
		# create a new node with those values and add it to the list
		tree_nodes.append(TreeNode(*new_values, children=base_nodes))
		# remove the old nodes from the list
		tree_nodes.remove(base_nodes[0])
		tree_nodes.remove(base_nodes[1])
		# make sure the tree nodes list is sorted
		tree_nodes = _sort_tree_nodes(tree_nodes)
		
	return tree_nodes[0]


def _get_addresses(root_node: TreeNode, char_list: list[str]):
	# recursively figure out the binary representation for all the characters
	addresses: dict[str, str] = {char: "" for char in char_list}
	
	def find_char(char: str, root: TreeNode):
		if char == root.char:
			return
		
		if char in root.children[0].char:
			addresses[char] += "0"
			find_char(char, root.children[0])
		else:
			addresses[char] += "1"
			find_char(char, root.children[1])
	
	for char in char_list:
		find_char(char, root_node)
		
	return addresses


def run() -> None:
	file_content: str = File.read(c.INPUT_FILE_PATH)
	
	char_freqs: dict[str, int] = _get_freq_dict(file_content)
	root_node: TreeNode = _create_tree(char_freqs)
	addresses: dict[str, str] = _get_addresses(root_node, list(char_freqs.keys()))
	
	# write the binary value to a string
	binary_string: str = ""
	
	for char in file_content:
		binary_string += addresses[char]
		
	# convert the string to an int
	binary_int: int = int(binary_string, 2)

	# convert the int to bytes
	binary_bytes: bytes = binary_int.to_bytes(ceil(len(binary_string)/8), byteorder='big')
	
	# Write the bytes to a binary file
	File.write_bin(c.OUTPUT_FILE_PATH, binary_bytes)
	
	