from collections import defaultdict
from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for i in words:
            dict_pattern = {}
            dict_word = defaultdict()
            index = 0
            flag = True
            for j in pattern:
                if j not in dict_pattern and i[index] not in dict_word:
                    dict_pattern[j] = i[index]
                    dict_word[i[index]] = j
                elif j in dict_pattern and i[index] in dict_word:
                    if dict_pattern[j] == i[index] and dict_word[i[index]] == j:
                        index += 1
                        continue
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
                index += 1
            if flag:
                ans.append(i)
        return ans
