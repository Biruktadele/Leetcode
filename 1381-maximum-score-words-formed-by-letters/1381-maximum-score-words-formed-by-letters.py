class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)

        def backtrack(index, current_score, available_letters):
            if index == len(words):
                return current_score
            
            max_score = backtrack(index + 1, current_score, available_letters)
            
            word = words[index]
            word_count = Counter(word)
            
            if all(available_letters[c] >= word_count[c] for c in word_count):
                for c in word_count:
                    available_letters[c] -= word_count[c]
                max_score = max(max_score, backtrack(index + 1, current_score + word_score(word), available_letters))
                for c in word_count:
                    available_letters[c] += word_count[c]
            
            return max_score

        return backtrack(0, 0, Counter(letters))