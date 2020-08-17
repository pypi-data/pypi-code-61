class Completer:
    def __init__(self, words):
        self.words = words

    def complete(self, prefix, i):
        self.matching_words = [w for w in self.words if w.startswith(prefix)]
        try:
            return self.matching_words[i]
        except:
            return None
