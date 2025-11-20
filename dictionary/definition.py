
class DictionaryDefinition:
	def __init__(self, definition_info: dict) -> None:
		self.definition: str | None = definition_info.get("definition", None)
		self.example: str | None = definition_info.get("example", None)
		self.synonyms: list[str] = definition_info.get("synonyms", [])
		self.antonyms: list[str] = definition_info.get("antonyms", [])

	def __repr__(self) -> str:
		return f"<DictionaryDefinition {self.definition}>"