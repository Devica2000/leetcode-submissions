class Codec:
    def encode(self, strs: List[str]) -> str:
        # add thye length followed by # before the start of the string
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s:str) -> List[str]:
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = s[i:j]
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res

























        #use this function to create
        #a single strip of all strings in list
        #add length and delimiter in the encoded string

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s:str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #extract the length from the encoded string
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length

        return res



#         """Encodes a list of strings to a single string.
#         """
#         res = ""
#         for s in strs:
#             res += str(len(s)) + "#" + s
#         return res

#     def decode(self, s: str) -> List[str]:
#         """Decodes a single string to a list of strings.
#         """
#         res = []
#         i = 0

#         while i < len(s):
#             j = i
#             while s[j] != "#":
#                 j += 1
#             length = int(s[i:j])
#             res.append(s[j+1:j+1+length])
#             i = j + 1 + length
#         return res
       
# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(strs))