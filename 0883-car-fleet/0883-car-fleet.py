class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d={}
        for i in range(len(position)):
            d[position[i]]=(target-position[i])/speed[i]
        di=dict(sorted(d.items(),key=lambda  x:-x[0]))
        mx=0
        cnt=0
        for i in di.values():
            if i>mx:
                mx=i
                cnt+=1
        return cnt

        

        