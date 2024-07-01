class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            preName, domain = email.split("@")[-2], email.split("@")[-1]
            localName = preName.split("+")[0].replace(".", "")
            emailSet.add(localName+"@"+domain)
        return len(emailSet)