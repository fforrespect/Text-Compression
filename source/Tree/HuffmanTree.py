from typing import Optional


class TreeNode:
	def __init__(self, char: str, frequency: int, children: tuple[Optional[object], Optional[object]] = (None, None)):
		self.char: str = char
		self.frequency: int = frequency
		self.children: tuple[Optional[TreeNode], Optional[TreeNode]] = children

	def __str__(self) -> str:
		return f"{repr(self.char)[1:-1].ljust(2, " ")}: {self.frequency}"

# class Tree:
# 	def __init__(self):
# 		pass
