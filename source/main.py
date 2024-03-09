
file_name: str = "inputText.txt"

with open(f"../resources/{file_name}", "r") as file:
	file_content: str = file.read()


char_freqs: dict[str, int] = {}

for char in file_content:
	if char in char_freqs:
		char_freqs[char] += 1
	else:
		char_freqs[char] = 1

print(char_freqs)
