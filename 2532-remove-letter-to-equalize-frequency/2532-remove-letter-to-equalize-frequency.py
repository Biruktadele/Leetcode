class Solution:
    def equalFrequency(self, word: str) -> bool:

        freq = sorted(Counter(word).values())  

        freq[0] -= 1 
        if len(set(filter(None, freq))) == 1: 
            return True

        freq[0] += 1 
        freq[-1] -= 1 
        return len(set(filter(None, freq))) == 1  
        
        