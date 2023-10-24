class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Reverse a string
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()
        
        return new_str == new_str[::-1]


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