class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        l = 0 
        r = len(skill) - 1
        ava = skill[l] + skill[r]
        prod = 0
        while l < r:
            if skill[l] + skill[r] != ava:
                return -1
            prod += (skill[l] * skill[r])
            l += 1
            r -= 1
        
        return prod

