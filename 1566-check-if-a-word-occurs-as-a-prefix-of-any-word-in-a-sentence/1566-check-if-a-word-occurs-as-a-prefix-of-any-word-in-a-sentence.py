class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
       
        sentence = sentence.split()
        searchWord = list(searchWord)
        length = len(searchWord)
        for j, i in enumerate(sentence):
       
            if len(i) < length:
                continue
            else:
                i = list(i)
       
                if i[0:length] == searchWord:
                    return j+1
        return -1
