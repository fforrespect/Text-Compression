from Meta.Process import get_freq_dict
from Meta import Constants as c, File


def run():
	file_content = File.get_content(c.INPUT_FILE_PATH)
	
	char_freqs: dict[str, int] = get_freq_dict(file_content)
	sorted_char_freqs: list[tuple[str, int]] = [(k, v) for k, v in sorted(char_freqs.items(), key=lambda item: item[1])]
	
	print(sorted_char_freqs)
	