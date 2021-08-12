import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        
        for element in intervals[1:]:
            if(free_rooms[0] <= element[0]):
                # make a room free since the next meeting starts after the min of all ongoing meeting's end time is completed
                heapq.heappop(free_rooms)
            # add next end time since the free room will be occupied by the next meeting and even if the previous meeting is completed after pop we need to push the new end time of the new meeting
            heapq.heappush(free_rooms, element[1])
            
        return len(free_rooms)
                
            