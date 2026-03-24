import time
import model as md
# import flet as ft # Flet is not used here


class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, sentence, language, modality):
        """
        Processes the input sentence, identifies wrong words,
        and calculates the time elapsed for the search.
        """

        # Clean the input text and convert it to lowercase
        sentence = replaceChars(sentence.lower())

        # Split the sentence into a list of words
        words = sentence.split()

        # Execute the chosen search algorithm and measure ONLY its execution time
        match modality:
            case "Default":
                t1 = time.time()
                rich_words = self._multiDic.searchWord(words, language)
                t2 = time.time()

            case "Linear":
                t1 = time.time()
                rich_words = self._multiDic.searchWordLinear(words, language)
                t2 = time.time()

            case "Dichotomic":
                t1 = time.time()
                rich_words = self._multiDic.searchWordDichotomic(words, language)
                t2 = time.time()

            case _: return None, 0

        # Build the string of wrong words OUTSIDE the match block
        # Using a Pythonic generator expression and .join() for cleaner and faster string building
        wrong_words = " ".join([str(rw) for rw in rich_words if not rw.correct])

        return wrong_words, t2 - t1


def replaceChars(text):
    """
    Removes punctuation and special characters from the input text.
    """
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text