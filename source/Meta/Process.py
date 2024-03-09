
def get_freq_dict(text: str) -> dict[str, int]:
	char_freqs: dict[str, int] = {}
	
	for char in text:
		if char in char_freqs:
			char_freqs[char] += 1
		else:
			char_freqs[char] = 1
	
	return char_freqs
