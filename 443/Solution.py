class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index = 1
        count = 1
        for i in range(1,len(chars)):
            if chars[i-1] == chars[i]:
                count += 1
            else:
                if count != 1:
                    for j in str(count):
                        chars[index] = j
                        index += 1
                count = 1
                chars[index] = chars[i]
                index += 1
        if count != 1:
            for j in str(count):
                chars[index] = j
                index += 1
        return index
