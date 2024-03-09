from typing import Optional


class TreeNode:
	def __init__(self, char: str, children: tuple[Optional[object], Optional[object]]):
		self.char: str = char
		self.children: tuple[Optional[TreeNode], Optional[TreeNode]] = children


# class Tree:
# 	def __init__(self):
# 		pass
