class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for char_s in s:
            if char_s not in dict_s:
                dict_s[char_s] = 1
            dict_s[char_s] += 1

        for char_t in t:
            if char_t not in dict_t:
                dict_t[char_t] = 1
            dict_t[char_t] += 1

        if dict_s == dict_t:
            return True
        
        return False
        






























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

        # return sorted(s) == sorted(t):

        # if Counter(s) == Counter(t):
        #     return True
        # else:
        #     return False


        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # #Use get to avoid key not found error
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        # return True