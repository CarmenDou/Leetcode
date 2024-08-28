class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f = [-1, -1]
        s = [-1, -1]
        res = 0
        for i in range(len(fruits)):
            if f == [-1, -1]:
                f = [i, i]
            elif fruits[f[0]] == fruits[i]:
                f[1] = i
            elif s == [-1, -1]:
                s = [i, i]
            elif fruits[s[0]] == fruits[i]:
                s[1] = i
            else:
                res = max(res, max(f[1], s[1])-min(f[0], s[0])+1)
                if f[1] > s[1]:
                    f = [s[1]+1, f[1]]
                    s = [i, i]
                else:
                    if f[1] < s[0]:
                        f = s
                        s = [i, i]
                    else:
                        f = [f[1]+1, s[1]]
                        s = [i, i]
        if s == [-1, -1]:
            return len(fruits)
        return max(res, max(f[1], s[1])-min(f[0], s[0])+1)
                    
