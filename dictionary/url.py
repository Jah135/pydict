BASE_DICTIONARY_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def gen_url(word: str) -> str:
	return BASE_DICTIONARY_URL + word