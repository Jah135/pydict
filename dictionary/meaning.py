from .partofspeech import PartOfSpeech
from .definition import DictionaryDefinition

class DictionaryMeaning:
	def __init__(self, meaning_info: dict) -> None:
		self.part_of_speech = PartOfSpeech(meaning_info.get("partOfSpeech", "unknown"))
		self.synonyms: list[str] = meaning_info.get("synonyms", [])
		self.antonyms: list[str] = meaning_info.get("antonyms", [])

		self.definitions: list[DictionaryDefinition] = [DictionaryDefinition(info) for info in meaning_info.get("definitions", [])]
	
	def __repr__(self) -> str:
		return f"<DictionaryMeaning {self.part_of_speech.name}, {len(self.definitions)} definitions>"