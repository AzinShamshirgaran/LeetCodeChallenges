class Solution:


   def kSmallestPairs(self, nums1, nums2, k: int) :
       dict={}
       lst_final=[]
       for i in nums1:
           for j in nums2:

               #dict[i+j] = [i,j]
               dict.setdefault(i+j, []).append([i,j])
       print(dict)
       lst =list(dict.keys())

       lst.sort()


       for u in lst[0:k]:

          lst_final.append(dict[u])
           #print(dict[lst(u)])
           #lst_final.append(dict(lst_sorted(u)))
       return lst_final




if __name__ == '__main__':
    num1=[1,1,2]
    num2=[1,2,3]
    k=3
    print(Solution().kSmallestPairs(num1,num2,k))