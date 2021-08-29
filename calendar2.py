class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlap:
            if(start<j and end>i):
                return False
        for i, j in self.calendar:
            if(start<j and end>i):
                self.overlap.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
        



# [None, True, True, False, False, True, False]
# [null,true,true,true,false,true,true]
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


cal = ["MyCalendarTwo","book","book","book","book","book","book"]
arr = [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
ans = []
obj = MyCalendarTwo()
ans.append(None)

for a in arr[1:]:
    # print(obj.book(a[0], a[1]))
    ans.append(obj.book(a[0], a[1]))
print(ans)

# [null,true,true,true,false,true,true]