class TimeMap:

    def __init__(self):
        #use a hashmap to store key:val pairs
        #key: a list of list: [[val, timestamp]]
        self.store = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        #check if the key does not exist
        if not key in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        #use binary search to look for the value 
        #for the key at a given timestamp
        
        #define the default return
        res = ""
        #return an empty list by default if the key does not exist
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1
        while l<= r:
            m = (l + r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)