from better_profanity import profanity

class WordChecker:
    def __init__(self,  custom_words=None):
        profanity.load_censor_words()
        if custom_words:
            profanity.load_censor_words(custom_words + list(profanity.CENSOR_WORDSET))

    async def is_badword(self, word:str) -> bool:
            return profanity.contains_profanity(word)

    async def check_phrase(self, phrase:str) -> bool:
        filtered_count = sum(1 for word in phrase if self.is_badword(word))
        return filtered_count

    async def check_word(self, word:str) -> bool:
        return self.check_phrase(word)



if __name__ == "__main__":
    # testing stuff
    from . import wordlist as wl
    checker = WordChecker(custom_words=wl)
    print(checker.check_word("hello"))  # False
    print(checker.check_word("helloo"))  # False
    print(checker.check_word("fuck"))  # True
    print(checker.check_phrase("hello world"))  # False
    print(checker.check_phrase("fuck you"))  # True
    print(checker.check_phrase("helloo world"))  # False