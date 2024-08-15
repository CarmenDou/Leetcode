class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = []
        for i in range(len(s)):
            if s[i] == "(":
                remove.append(i)
            elif s[i] == ")":
                if remove and s[remove[-1]] == "(":
                    remove.pop()
                else:
                    remove.append(i)
        res = ""
        for i in range(len(s)):
            if i not in remove:
                res += s[i]
        return res


