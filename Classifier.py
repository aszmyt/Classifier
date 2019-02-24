from GenerateVector import Generator
from nltk.tokenize import word_tokenize
from pathlib import Path
import nltk
import pickle

N=100

g = Generator()
all_words = g.GetResult(N)
g.SaveResult2ARFF(N)

fset = []
for directory in Path("./bbc").glob('*'):
    category = directory.parts[-1]
    pathlist = Path(directory).glob("./*.txt")
    for path in pathlist:
        with open(path, 'r') as file:
            raw = file.read()
            tokens = word_tokenize(raw)
            words = []
            for w in tokens:
                words.append(w.lower())
            feat = {}
            for w in all_words:
                feat[w[1]] = w[1] in words
            fset.append((feat, category))
            
classifier = nltk.NaiveBayesClassifier.train(fset)
print("---> Accuracy:",(nltk.classify.accuracy(classifier, fset)*100))
fset_words = fset
print(classifier.classify_many([words for (words, cat) in fset[:10]]))
classifier.show_most_informative_features(5)

f = open('classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()