class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] *(n+1)
        for i in shifts:
            if i[2] == 1: 
                arr[i[0]] += 1
                arr[i[1]+1] -= 1
            else:
                arr[i[0]] -= 1
                arr[i[1]+1] += 1
        print(arr)
        for i in range(1, n):
            arr[i] += arr[i-1]
        st = []
        print(arr)
        for j , i in enumerate(s):
            n = arr[j]%26
            new_word = chr(((ord(i)-ord('a'))%26 + n)%26+ord('a') )
            st.append(new_word)
        return "".join(st)
    