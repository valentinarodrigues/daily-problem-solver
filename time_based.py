from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        search_hashMap = self.hashMap[key]
        ans = -1
        left, right, ans = 0, len(search_hashMap)-1, -1
        while(left<=right):
            mid = (left+right)//2
            if(search_hashMap[mid][1] <= timestamp):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        if ans == -1: return ""
        return search_hashMap[ans][0]

result = []


commands = ["TimeMap","set","set","get","get","get","get","get"]
values = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]


for c,v in zip(commands, values):
    if(c == "TimeMap"):
        # initialize array
        obj = TimeMap()
        result.append(None)
    elif(c == "set"):
        # set
        key = v[0]
        value = v[1]
        timestamp = v[1]
        result.append(obj.set(key, value, timestamp))
    elif(c == "get"):
        result.append(obj.get(key,timestamp))
print(result)