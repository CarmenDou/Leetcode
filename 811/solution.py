from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # dic = defaultdict(int)
        # for cpdomain in cpdomains:
        #     tmp = cpdomain.split()
        #     count,subdomains = int(tmp[0]),tmp[1].split(".")
        #     i = 0
        #     while i < len(subdomains):
        #         subdomain = ".".join(subdomains[i:])
        #         dic[subdomain] += count
        #         i += 1
        # res = []
        # for key,value in dic.items():
        #     res.append(str(value) + " " + key)
        # return res

        counter=defaultdict(int)
        for count_domain in cpdomains:
            count,domain=count_domain.split(" ")
            domains=domain.split(".")
            string=''
            for i in range(len(domains)):
                counter[".".join(domains[i:])]+=int(count)
                
        return ["{} {}".format(count,string) for string,count in counter.items()]


        
        