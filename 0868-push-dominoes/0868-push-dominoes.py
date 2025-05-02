class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def fill(l , r , past):
            if past == "R" and r < len(dominoes) and dominoes[r] == "L":
                l += 1
                r -= 1
                while l < r:
                    arr[l] = "R"
                    arr[r] = "L"
                    l += 1
                    r -= 1
            elif not past and dominoes[r] == "L":
                r -= 1
                while r >= 0:
                    arr[r] = "L"
                    r -= 1
            elif dominoes[l] == "R" and r == len(dominoes):
                l += 1
                while l < r:
                    arr[l] = "R"
                    l += 1
            elif dominoes[l] == "R":
                l += 1
                while l < r:
                    arr[l] = "R"
                    l += 1
            elif dominoes[r] == "L":
                r -= 1
                while r >= l:
                    arr[r] = "L"
                    r -= 1


        arr = list(dominoes)
        # print(arr)
        past = ""
        l = 0
        r = 0
        while r < len(dominoes):
            if dominoes[r] != ".":
                fill(l , r , past)
                l = r
                past = dominoes[r]
            r += 1
        if past == "R":
            fill(l , r , past)
        return "".join(arr)