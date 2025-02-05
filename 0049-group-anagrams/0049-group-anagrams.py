class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in range(len(strs)):
            d["".join(sorted(strs[i]))].append(strs[i])
        return list(d.values())
        