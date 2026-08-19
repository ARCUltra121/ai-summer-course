class LyricAnalyzer():
    def __init__(self, lyrics:str):
        self.lyrics:str = lyrics
        punctuation = ":;,./!\"\'"
        for punct in punctuation:
            lyrics = lyrics.replace(punct, "")
        self.words = lyrics.lower().split()

    def count_words(self):
        result = {}

        for word in self.words:
            if word not in result:\
                result[word] = 1
            else:
                result[word] += 1
        return result



        _____________________________________________________
class LyricAnalyzer:
    def __init__(self, lyrics):
        self.lyrics = lyrics
        punctuation = ".,!?;:'\"()-[]{}"
        cleaned_lyrics = lyrics.lower()

        for character in punctuation:
            cleaned_lyrics = cleaned_lyrics.replace(character, "")

        self.words = cleaned_lyrics.split()

    def count_words(self):
        counts = {}

        for word in self.words:
            counts[word] = counts.get(word, 0) + 1

        return counts

    def unique_word_count(self):
        return len(set(self.words))

    def most_common_word(self):
        counts = self.count_words()

        if not counts:
            return "", 0

        return max(counts.items(), key=lambda item: item[1])

    def print_report(self):
        counts = self.count_words()

        print("=== WORD COUNT ===")

        for word in sorted(counts):
            print(f"{word:<12}: {counts[word]}")

        print()
        print(f"Unique words: {self.unique_word_count()}")

        word, count = self.most_common_word()
        print(f"Most common word: '{word}' — {count} times")

    def filter_stopwords(self, stop_words):
        self.words = [
            word for word in self.words
            if word not in stop_words
        ]


if __name__ == "__main__":
    lyrics = """
    we will we will rock you
    we will we will rock you
    buddy youre a boy make a big noise
    playing in the street gonna be a big man someday
    you got mud on your face you big disgrace
    kicking your can all over the place singing
    we will we will rock you
    """

    analyzer = LyricAnalyzer(lyrics)

    analyzer.print_report()

    stop_words = {
        "a",
        "the",
        "you",
        "your",
        "in",
        "on",
        "we",
        "be",
        "got"
    }

    analyzer.filter_stopwords(stop_words)

    print()
    print("=== FILTERED WORD COUNT ===")
    analyzer.print_report()