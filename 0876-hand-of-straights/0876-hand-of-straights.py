class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        d = {}

        for i in hand:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # hand = set(hand)
        for i in hand:
            if i in d:
                for j in range(groupSize):
                    x = i+j
                    if x in d:
                        if d[x] == 1:
                            d.pop(x)
                        else:
                            d[x] -= 1
                    else:
                        return False
                        
        return True