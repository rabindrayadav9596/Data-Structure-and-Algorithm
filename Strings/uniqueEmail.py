class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = []
        for i in range(len(emails)):
            atIndex = emails[i].find('@')
            pIndex = emails[i].find('+')
            temp = ""
            if(pIndex != -1):
                temp = emails[i][:pIndex]
            else:
                temp = emails[i][:atIndex]
            temp = temp.replace('.', '')
            email = temp+emails[i][atIndex:]
            if email not in uniqueEmails:
                uniqueEmails.append(email)

        return len(uniqueEmails)
