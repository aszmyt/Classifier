from SelfExtendingDictionary import SelfExtendingDictionary as Dict
from pathlib import Path
import re
import json


class Generator:

    def __init__(self, *args, **kwargs):
        self.TopicMaps = dict()
        self.ProcessedData = dict()
        self.Result = []
        dirs = Path("./bbc").glob("*")
        for directory in dirs:
            topic_name = directory.parts[-1]
            self.TopicMaps[topic_name] = Dict()
            self._IterateOverFiles(directory, topic_name)
    
    def GetResult(self, length):
        if self.ProcessedData and len(self.ProcessedData[next(iter(self.ProcessedData))]) == length:
            return self.Result
        self._SortAll(length)
        for topic in self.ProcessedData:
            #print(self.ProcessedData[topic])
            self.Result = self.Result + [(topic, word) for (word, count) in self.ProcessedData[topic]]
        return self.Result

    def _MapInFileWords(self, file, topic_name):
        for line in file:
            for word in line.split():
                word = re.sub('[^A-Za-z]+', '', word)
                self.TopicMaps[topic_name].add(word.lower())


    def _IterateOverFiles(self, directory, topic_name):
        pathlist = Path(directory).glob("./*.txt")

        for path in pathlist:
            with open(path, 'r') as f:
                self._MapInFileWords(f, topic_name)

    def _SortAll(self, length):
        for topic in self.TopicMaps:
            self.TopicMaps[topic].remove_common()
            self.ProcessedData[topic] = self._Map2SortedList(self.TopicMaps[topic])
            self.ProcessedData[topic] = [p for p in self.ProcessedData[topic][0:length]]


    def _Map2SortedList(self, dictionary):
        return sorted(dictionary.items(), key = lambda x: x[1], reverse = True)

    def SaveResult2ARFF(self, length):
        output_filename = "./WektorCech.arff"
        output_filenameJSON = "./WektorCech.json"
        with open(output_filename,"w") as fp:
            fp.write('''@RELATION wordcounts\n@ATTRIBUTE word string\n@DATA\n''')
            for word in self.GetResult(length):
                
                fp.write("%s, %s\n" % (word[1], word[0]))
        with open(output_filenameJSON,"w") as fp:
            json.dump(self.Result, fp)

if __name__ == "__main__":
    g = Generator()
    result = g.GetResult(100)
    #print(result)