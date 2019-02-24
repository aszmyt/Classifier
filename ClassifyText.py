from nltk.tokenize import word_tokenize
from pathlib import Path
import pickle
import json
import nltk

all_words = []
with open("./WektorCech.json", 'r') as fp:
    all_words = json.load(fp)
all_words = [word[1] for word in all_words]

def main():

    file2catmap = []
    fset = []
    for directory in Path("./test").glob('*'):
        category = directory.parts[-1]
        pathlist = Path(directory).glob("./*.txt")
        for path in pathlist:
            filename = path.parts[-1]
            file2catmap.append((filename,category))
            with open(path, 'r') as file:
                raw = file.read()
                tokens = word_tokenize(raw)
                words = []
                for w in tokens:
                    words.append(w.lower())
                feat = {}
                for w in all_words:
                    feat[w] = w in words
                fset.append((feat, category))

    f = open('classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

    #fset = [w for (w,c) in fset]
    #classified = (classifier.classify_many(fset))
    #for i in range(0, len(classified)):
    #    file2catmap[i] = (file2catmap[i], classified[i])
    #print(file2catmap)
    accuracy = (nltk.classify.accuracy(classifier, fset)*100)
    print("---> Accuracy:",accuracy)



if __name__ == "__main__":
    main()