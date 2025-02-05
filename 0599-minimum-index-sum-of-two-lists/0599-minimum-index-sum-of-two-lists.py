class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        d2 = defaultdict(list)
    
        mn = len(list1) + len(list2)
        for i in range(len(list1)):
            if list1[i] not in d1:
                d1[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in d1:
                if j+d1[list2[j]] <= mn:
                    mn = j+d1[list2[j]]
                    d2[mn].append(list2[j])
        ans = []
        for i in d2[mn]:
            ans.append(i)
        return ans



        