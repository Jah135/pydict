from requests import get as _get

from .meaning import DictionaryMeaning
from .url import gen_url

class DictionaryWordEntry:
	def __init__(self, entry_info: dict) -> None:
		self.word: str | None = entry_info.get("word", None)
		self.phonetic: str | None = entry_info.get("phonetic", None)

		self.meanings: list[DictionaryMeaning] = [DictionaryMeaning(info) for info in entry_info.get("meanings", [])]
	
	def __repr__(self) -> str:
		return f"<DictionaryWordEntry {self.word}>"

class DictionaryWord:
	def __init__(self, word_info: list) -> None:
		self.entries: list[DictionaryWordEntry] = [DictionaryWordEntry(info) for info in word_info]
	
	def __repr__(self) -> str:
		return f"<DictionaryWord {len(self.entries)}>"

def get_word_info(word: str) -> DictionaryWord:
	response = _get(gen_url(word))

	return DictionaryWord(response.json())