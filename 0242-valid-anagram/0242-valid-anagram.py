class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for elem in s:
            if elem not in count_s:
                count_s[elem] = 1
            else:
                count_s[elem] += 1

        for val in t:
            if val not in count_t:
                count_t[val] = 1
            else:
                count_t[val] += 1

        if count_s == count_t:
            return True
        return False

        # # Compare counts
        # for key in count_s:
        #     if key not in count_t or count_s[key] != count_t[key]:
        #         return False
        
        # # If all keys match, return True
        # return True

        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # if Counter(s) == Counter(t):
        #     return True
        # else:
        #     return False


        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        #Use get to avoid key not found error
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True