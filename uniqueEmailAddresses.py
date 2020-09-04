#https://leetcode.com/explore/interview/card/google/67/sql-2/3044/


class Solution:
    def numUniqueEmails(self, emails):
        list_f=[]
        for email in emails:
            #print(email)
            index= email.find('@')
            #print(index)
            Str= list(email)
            #print(Str)
            local_name = Str[:index]
            #print(local_name)
            domain_name = Str[index+1:]
            #print(domain_name)
            local_name_f=[]
            for i in range(len(local_name)):
                if local_name[i]!='.':
                    if local_name[i]=='+':
                        break
                    else:
                        local_name_f.append(local_name[i])




            email = local_name_f +['@']+ domain_name
            #print (email)
            if email not in list_f:
                list_f.append(email)
        return len(list_f)




if __name__ == '__main__':
            S = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

            print(Solution().numUniqueEmails(S))