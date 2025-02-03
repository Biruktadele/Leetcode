class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player = defaultdict(int)
        for i in matches:
            player[i[1]] += 1
            player[i[0]] += 0
        no_loss = []
        one_loss = []
        for i in player:
            if player[i] == 0:
                no_loss.append(i)
            elif player[i] == 1:
                one_loss.append(i)
        no_loss.sort()
        one_loss.sort()
        return [no_loss,one_loss]


        