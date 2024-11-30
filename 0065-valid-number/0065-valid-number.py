class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        l = len(s)
        d = {'e' : 0,'.' : 0}

        for i,k in enumerate(s):
            if k.isdigit():
                continue
            elif k == '.':
                d[k] += 1
                if l == 1:
                    return False
                elif s[i-1].isdigit() and d['e'] == 0 and d[k] == 1:
                    continue
                elif i == l-1:
                    return False
                elif i < l-1 and( d[k] > 1 or d['e'] > 0 or not s[i+1].isdigit()):
                    return False

            elif k == 'e':
                
                if i == 0 or (i == 1 and ord(s[0]) not in range(ord('0') , ord('9')+1)) or d[k] > 0 or (i == 2 and (s[0] == '+' or s[0] == '-') and (ord(s[1]) not in range(ord('0') , ord('9')+1))):
                    print("yes")
                    return False
                elif i == l-1:
                    return False
            
                d[k] += 1
            elif k == '-' or k == '+':
                if i == 0 and i < l-1 and (s[i+1].isdigit() or s[i+1] == '.'):
                    continue
                elif s[i-1] == 'e' and i < l-1 and s[i+1].isdigit():
                    continue
                else:
                    return False
            else:
                return False
        return True
        



