from collections import defaultdict
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # dic = defaultdict(int)
        # for word in words:
        #     trans_word = ""
        #     for i in word:
        #         trans_word += code[ord(i)-97]
        #     dic[trans_word] += 1
        # return len(dic)  

        #学习怎么用zip
        code = {string:code for string,code in zip("abcdefghijklmnopqrstuvwxyz",[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}
        dic = defaultdict(int)
        for word in words:
            key = "".join([code[char] for char in word])
            dic[key] += 1
        return len(dic)
