from Meta.Process import get_freq_dict
from Meta import Constants as c, File
from Tree.HuffmanTree import TreeNode


def _sort_tree_nodes(tree_nodes: list[TreeNode]) -> list[TreeNode]:
	return sorted(tree_nodes, key=lambda item: item.frequency)


def run() -> None:
	file_content = File.get_content(c.INPUT_FILE_PATH)
	
	char_freqs: dict[str, int] = get_freq_dict(file_content)
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
	
	addresses: dict[str, str] = {char: "" for char in char_freqs.keys()}
	
	def find_char(char: str, root: TreeNode):
		if char == root.char:
			return
		
		if char in root.children[0].char:
			addresses[char] += "0"
			find_char(char, root.children[0])
		else:
			addresses[char] += "1"
			find_char(char, root.children[1])
			
	for char in char_freqs.keys():
		find_char(char, tree_nodes[0])
	
	print(addresses)
	