class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.isspace() == True:
            return True
        s = s.lower()
        new_str = ""
        for char in s:
            if char.isalnum() == True:
                new_str += char
            else:
                continue

        l = 0
        r = len(new_str) - 1

        while l < r:
            if new_str[l] == new_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

            

       