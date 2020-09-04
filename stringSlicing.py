class Solution:
    def stringSlice(self, S, beg, end):
        if not S:
            return 0
        print(S[:3])
        print(S[3:])
        return S[beg:end]



if __name__ == '__main__':
            S = "azin joon"
            beg=2
            end=-2

            print(Solution().stringSlice(S, beg, end))