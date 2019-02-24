from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class SelfExtendingDictionary(dict):
    """
    Standard dict extended with add functionality.
    """
    wnl = WordNetLemmatizer()

    def add(self, key):
        """
        We assume we have sting to int map. When key is added value is set to 1.
        Each time added key already exist value is increased by 1.
        """
        if key == '':
            return
        key = self._key_lemmatizer(key)
        if key in self:
            self[key] = self[key] + 1
        else:
            self[key] = 1

    def remove_common(self):
        # stop_words = set(stopwords.words("english"))
        # for word in stop_words:
        #     if word in self:
        #         del self[word]
        with open("./common_words.txt", 'r') as common:
            for line in common:
                for word in line.split():
                    lematized = SelfExtendingDictionary.wnl.lemmatize(word.lower())
                    if lematized in self:
                        del self[lematized]

    def _key_lemmatizer(self, word):
        return SelfExtendingDictionary.wnl.lemmatize(word)

