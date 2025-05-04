from . import wordlist as wl

wordlist = wl.wordlist

FILTERED_WORDS = set(word.lower() for word in wordlist)

async def check(text):
    words = text.lower().split()
    filtered_count = sum(1 for word in words if word in FILTERED_WORDS)
    return filtered_count