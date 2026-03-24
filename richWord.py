
class RichWord:
    def __init__(self, word):
        self._word = word # this is a string
        self._correct = None # this is a bool

    @property # getter
    def correct(self):
        return self._correct

    @correct.setter # setter
    def correct(self, bool_value):
        self._correct = bool_value

    @property # getter
    def word(self):
        return self._word

    def __str__(self):
        return self._word