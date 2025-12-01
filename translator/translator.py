# translator/translator.py

from deep_translator import GoogleTranslator


class Translator:
    """
    Object-oriented translator that converts English words into another language.
    Default: German ("de").
    """

    def __init__(self, source_lang="en", target_lang="de"):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslator(
            source=self.source_lang, 
            target=self.target_lang
        )

    def translate_one(self, word: str) -> str:
        """Translate a single English word."""
        return self.translator.translate(word)

    def translate_many(self, word_list: list[str]) -> list[str]:
        """Translate a list of English words at once."""
        return self.translator.translate_batch(word_list)
# translator/test_translator.py



def test_translator():
    # Instantiate
    tr = Translator(target_lang="de")

    # Test single
    print("desk  ->", tr.translate_one("desk"))
    print("chair ->", tr.translate_one("chair"))

    # Test batch
    words = ["desk", "chair", "floor", "board"]
    translated = tr.translate_many(words)

    print("\nBatch:")
    for en, de in zip(words, translated):
        print(f"{en:10s} -> {de}")

if __name__ == "__main__":
    test_translator()
