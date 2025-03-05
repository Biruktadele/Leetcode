class RecentCounter:

    def __init__(self):
        self.q = deque([])
        

    def ping(self, t: int) -> int:
        if self.q:
            buttom = self.q[0]
            # top = self.q[-1]
            while self.q and t - buttom > 3000:
                self.q.popleft()
                if self.q:
                    buttom = self.q[0]
        self.q.append(t)
        return len(self.q)
            

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)