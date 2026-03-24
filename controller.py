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

        # String to accumulate misspelled words
        wrong_words = " - "

        match modality:
            case "Default":
                t1 = time.time()
                rich_words = self._multiDic.searchWord(words, language)

                for rw in rich_words:
                    if not rw.correct:
                        wrong_words += str(rw) + " - "

                t2 = time.time()
                return wrong_words, t2 - t1

            case "Linear":
                t1 = time.time()
                rich_words = self._multiDic.searchWordLinear(words, language)

                for rw in rich_words:
                    if not rw.correct:
                        wrong_words += str(rw) + " - "

                t2 = time.time()
                return wrong_words, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                rich_words = self._multiDic.searchWordDichotomic(words, language)

                for rw in rich_words:
                    if not rw.correct:
                        wrong_words += str(rw) + " - "

                t2 = time.time()
                return wrong_words, t2 - t1

            case _: return None

    def printMenu(self):
        """
        Prints the CLI menu (kept for backwards compatibility with Lab 03).
        """
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    """
    Removes punctuation and special characters from the input text.
    """
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text