class node:
    def __init__(self, homepage: str):
        self.val = homepage
        self.next = None
        self.pre = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = node(homepage)
        

    def visit(self, url: str) -> None:
        new = node(url)
        new.pre = self.head
        self.head.next = new
        self.head = new
        
    def back(self, steps: int) -> str:
        while self.head.pre and steps:
            self.head = self.head.pre
            steps -= 1
        return self.head.val
    def forward(self, steps: int) -> str:
        while self.head.next and steps:
            self.head = self.head.next
            steps -= 1
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)