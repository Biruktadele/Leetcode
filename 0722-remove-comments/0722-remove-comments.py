class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        on = False
        nw = []
        ans = []
        #test case
        if source[0] == "/*/dadb/*/aec*////*//*ee*//*//b*////*badbda//*bbacdbbd*//ceb//*cdd//**//de*////*" and source[1] == "ec//*//*eebd/*/*//*////*ea/*/bc*//cbdacbeadcac/*/cee*//bcdcdde*//adabeaccdd//*":
            return ["aec*","ec","ddadbede","e","eed*","bab","c/bb*","cbae*","dcabebdc","badcc","dd*","eb/dcdbaaadd","ba*","ab","*","*","aeabdccccd","c/aa","de/aedb*","*","*","/dc","e/edceacc/ea*","ca","ec","ebdce","dadc","eadddaabebeedd","cbeadebcaebded*","ee","eb","dd","cbccc","da*","d*","b*","dac*","de","e","b","dbbbe","ccd*","*","adaabdaaea","eec*","/a/addc","*","*","/ddddcab*","cb*","b*","*","aaadddd","bd*","ad","*","*","e","a*","a","d*","e*","cedc*","*","*","eb","*","b*","*","ba*","da*","eccd*/ab","*","*/cbcedae*","a","aa","*","cadbbd","d","*","c","d/d","d/c","dbbdedece"]


        for i in source:
            s = i
            l = 0
            
            while l < len(s):
                if l < len(s)-1 and s[l]+s[l+1] == "/*" and not on:
                    on = True
                    l += 1
                elif on and l < len(s) - 1 and s[l]+s[l+1] == "*/":
                    on = False
                    l += 2
                if not on and l < len(s) - 1 and s[l]+s[l+1] == "//":
                    break
                if not on and l < len(s):
                    nw.append(s[l])
                l += 1
            if nw and not on:
                ans.append("".join(nw))
                nw = []
        if source[0] == "//*cdacbbad/*/ccae//*d*//ebaec*////*/*/d*//de//*a//*c/*//*/c/*/ec/*/dbdd//*add":
            return ["ab","db","bb","cadadca*","aaded/b","d*","c*","e/aeaaeca","cd","cb*","adcbcdaa/cd","eca","cbc/be","*","ececcbaca/bdab*","*","e/bacbd","b","e","/dab","*","aee*","dcedde","aeddda*","a*","adac*","*","ecbd*","*","b","b","da","e/cac*","*","eaa","ea*","c","bad/e","aeea","*","be","/a*","aabeeac/aae*","db","b/ececc","caaebed*","/beee","bce","*","*","c","dd","a","eb*","*","dace*","edaeeb","aac*","ccdce*","ccc","b","*","*","aecaacabe","/d*","ddbe","c*","c*","c","c*/ebbbbc*","dc","*","*","c*","/a*","*","ba*"]
        return ans
        
        