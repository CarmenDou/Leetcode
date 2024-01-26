class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count = 0
        # dic = {'':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # last_char = ''
        # for char in s:
        #     if dic[last_char] < dic[char]:
        #         count = count - 2*dic[last_char] + dic[char]
        #     else:
        #         count += dic[char]
        #     last_char = char
        # return count

        # count = 0
        # dic = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        # i = 0
        # count = 0
        # while i < len(s):
        #     if i+1 < len(s) and s[i:i+2] in dic:
        #         count += dic[s[i:i+2]]
        #         i += 2
        #     elif s[i:i+1] in dic:
        #         count += dic[s[i:i+1]]
        #         i += 1
        # return count

        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=d[s[-1]]
        
        s=s[::-1]
        
        for i in range (len(s)-1):
            if d[s[i]]>d[s[i+1]]:
                res-=d[s[i+1]]
            else:
                res+=d[s[i+1]]
            
        return res



        