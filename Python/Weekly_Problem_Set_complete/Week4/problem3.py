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