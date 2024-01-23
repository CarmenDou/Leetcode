from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        self.dic=defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dic[key].append((value,timestamp))
        return True
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.dic:
            return ""
        else:
            #顺序查找超时
            # res = ""
            # list_key = self.dic[key]
            # i = 0
            # while i < len(self.dic[key]):
            #     if list_key[i][1] > timestamp:
            #         break
            #     i += 1
            # if i != 0:
            #     res = list_key[i-1][0]
            # return res

            #本身是有序的情况下可以binary search
            values = self.dic[key]
            low,high,n = 0, len(values)-1,len(values)-1
            while low <= high:
                mid = (low+high)//2
                if values[mid][1] > timestamp:
                    high = mid-1
                else:
                    if mid == n or values[mid+1][1] >timestamp:
                        return values[mid][0]
                    else:
                        low = mid + 1
            return ""

            # Tracy的binary search
            # values=self.dic[key]
            # low,high,n = 0,len(values)-1,len(values)-1
            # while low <= high:
            #     mid = low + (high - low) // 2
            #     if values[mid][1] > timestamp:
            #         high = mid - 1
            #     else:
            #         if mid ==n  or values[mid+1][1] > timestamp:
            #             return values[mid][0]
            #         else:
            #             low = mid + 1
        
            # return ""
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)