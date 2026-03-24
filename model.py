import dictionary as d
import richWord as rw


class MultiDictionary:
    def __init__(self):
        # Initialize dictionaries
        self._italian_dict = d.Dictionary(language="italian")
        self._italian_dict.loadDictionary("resources/Italian.txt")

        self._english_dict = d.Dictionary(language="english")
        self._english_dict.loadDictionary("resources/English.txt")

        self._spanish_dict = d.Dictionary(language="spanish")
        self._spanish_dict.loadDictionary("resources/Spanish.txt")

    def _selectDictionary(self, language):
        """
        Helper method to retrieve the correct dictionary list based on language.
        This avoids code repetition in the search algorithms.
        """
        if language == "Italian":
            return self._italian_dict.dictionary
        elif language == "English":
            return self._english_dict.dictionary
        elif language == "Spanish":
            return self._spanish_dict.dictionary
        else:
            raise ValueError(f"Lingua '{language}' non supportata.")

    def searchWord(self, words, language):
        """
        Default search using the 'in' operator (__contains__).
        Returns a list of RichWord objects.
        """
        rich_words = []
        selected_dictionary = self._selectDictionary(language)

        for word in words:
            rich_word = rw.RichWord(word)

            # Using Python's 'in' operator which leverages the __contains__ method under the hood
            if rich_word.word in selected_dictionary:
                rich_word.correct = True
            else:
                rich_word.correct = False

            rich_words.append(rich_word)

        return rich_words

    def searchWordLinear(self, words, language):
        """
        Linear search algorithm.
        Iterates over all vocabulary elements starting from the first.
        """
        rich_words = []
        selected_dictionary = self._selectDictionary(language)

        for word in words:
            rich_word = rw.RichWord(word)
            rich_word.correct = False  # Assume the word is incorrect initially

            # Linear search
            for elem in selected_dictionary:
                if rich_word.word == elem:
                    rich_word.correct = True  # Found!
                    break  # Stop searching this word

            rich_words.append(rich_word)

        return rich_words

    def searchWordDichotomic(self, words, language):
        """
        Dichotomic (binary) search algorithm.
        Takes advantage of the alphabetically sorted dictionary by splitting
        the search space in half at each iteration.
        """
        rich_words = []
        selected_dictionary = self._selectDictionary(language)

        for word in words:
            rich_word = rw.RichWord(word)
            rich_word.correct = False

            # Binary search pointers
            start = 0
            end = len(selected_dictionary) - 1

            while start <= end:
                middle = (start + end) // 2  # Recalculated at each iteration

                if rich_word.word == selected_dictionary[middle]:
                    rich_word.correct = True  # Found, stop the search
                    break
                elif rich_word.word < selected_dictionary[middle]:
                    # The word comes before alphabetically: discard the second half
                    end = middle - 1
                else:
                    # The word comes after alphabetically: discard the first half
                    start = middle + 1

            rich_words.append(rich_word)

        return rich_words
