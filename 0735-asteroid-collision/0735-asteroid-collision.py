class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stuck = []
        for i in asteroids:
            while stuck and i < 0 and stuck[-1] > 0:
                diff = stuck[-1] + i
                if diff < 0:
                    stuck.pop()
                elif diff == 0:
                    i = 0
                    stuck.pop()
                else:
                    i = 0
            if i: 
                stuck.append(i)           
        return stuck
        