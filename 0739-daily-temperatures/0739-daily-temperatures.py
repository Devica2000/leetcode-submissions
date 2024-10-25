class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair:[temp, index]

        for i,t in enumerate(temperatures):
            #check if the stack is non empty
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append([t, i])
        res
        












        # O(n) time and space complexity
        # result - to store the wait days at ith position
        # stack - to add pair of temp, idx from temperatures

        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            # check if the stack is non empty
            # then check if the last added element
            # is smaller than the current element
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append([temp,idx])
        return res

        #brute force - O(n^2)
        # wait_days = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             days = j - i
        #             break
        #         else:
        #             days = 0
        #     if i == len(temperatures) -1:
        #         days = 0
        #     wait_days[i] = days
        # return wait_days
        
        # O(n^2) and O(1)
        # for i in range(len(temperatures)):
        #     days = 0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             days = j - i
        #             break
        #     temperatures[i] = days
        # return temperatures