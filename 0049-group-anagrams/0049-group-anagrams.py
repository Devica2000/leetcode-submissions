class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_count = defaultdict(list) #mapping char count to values in strs

        for s in strs:
            #create a list of length 26 for char count
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            dict_count[tuple(count)].append(s)

        return list(dict_count.values())


        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26

        #     for c in s:
        #         count[ord(c) - ord("a")] += 1

        #     res[tuple(count)].append(s)

        # return res.values()

        # #Brute Force - O(n^2)
        # # Use sorting - sort the original list
        # # Compare the elements of the sorted list
        # # If they are equal, append to empty list as a list
        # # Else append [elem]

        # sorted_str = [''.join(sorted(s)) for s in strs]

        # #list to store output
        # output = []

        # #set to keep track of already matched elements
        # matched_set = set()

        # for i in range(len(sorted_str)):
        #     # check if i is not present in the matched set
        #     # add i to the group 
        #     if i not in matched_set:
        #         group = [strs[i]]
        #         for j in range(i+1, len(sorted_str)):
        #             if sorted_str[i] == sorted_str[j]:
        #                 group.append(strs[j])
        #                 matched_set.add(j)
        #         output.append(group)
        # return output

        # Time Complexity - O(n*mlogm)

        # anagram_dict = {}

        # for s in strs:
        #     sorted_strs = ''.join(sorted(s))
        #     if sorted_strs in anagram_dict:
        #         anagram_dict[sorted_strs].append(s)
        #     else:
        #         anagram_dict[sorted_strs] = [s]
        # return list(anagram_dict.values())

        #Time Complexity O(m*n*26)

        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())
