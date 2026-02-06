class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join(filter(str.isalnum, s)).lower()
        # print(s_new)

        if s == " ":
            return True

        str_1 = ""
        for i in range(len(s_new) - 1, -1, -1):
            str_1 += s_new[i]

        if s_new == str_1:
            return True
        else:
            return False


        # start = 0
        # end = len(s_new) - 1

        # for i in range(len(s_new)):























        #Using two pointer approcach and a custom helper function
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1 
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9')))
        #Using built in python functions
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]











        # Time Complexity = O(n)
        # Space Complexity - O(1)
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alnum(s[l]):
                l += 1
            while r > l and not self.alnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        # helper function to check if a character is alphanumeric
    def alnum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or 
        (ord('a') <= ord(c) <= ord('z')) or
        (ord('0') <= ord(c) <= ord('9')))

        # Reverse a string
        # # Time and space Complexity = O(n)
        # new_str = ""

        # for c in s:
        #     if c.isalnum():
        #         new_str += c.lower()
        
        # return new_str == new_str[::-1]


        # Time & Space Complexity = O(n)
        # if s.isspace() == True:
        #     return True
        # new_str = ""
        # for char in s:
        #     if char.isalnum():
        #         new_str += char.lower()
        #     else:
        #         continue

        # l = 0
        # r = len(new_str) - 1

        # while l < r:
        #     if new_str[l] == new_str[r]:
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        # return True 