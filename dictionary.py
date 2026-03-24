
class Dictionary:
    def __init__(self, dictionary=None, language=""):
        if dictionary is None:
            dictionary = []
        self._dictionary = dictionary
        self._language = language

    def loadDictionary(self, path):
        with open(path, "r", encoding="utf-8") as infile:
            for line in infile:
                self.dictionary.append(line.strip().lower())

    @property # getter
    def dictionary(self):
        return self._dictionary