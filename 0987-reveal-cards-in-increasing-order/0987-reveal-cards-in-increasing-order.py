class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        q = deque([deck[0]])

        for i in range(1,len(deck)):
            num = deck[i]
            removed = q.pop()
            q.appendleft(removed)
            q.appendleft(num)
        return list(q)

        