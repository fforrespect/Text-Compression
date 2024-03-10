
def read(file_path: str) -> str:
	with open(file_path, "r") as file:
		return file.read()


def write_bin(file_path: str, binary_data: bytes) -> None:
	with open(file_path, "wb") as file:
		file.write(binary_data)