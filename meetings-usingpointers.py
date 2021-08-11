class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = sorted(i[0] for i in intervals)
        end_time = sorted(i[1] for i in intervals)
        strt_idx = 0
        end_idx = 0
        used_rooms = 0
        while(strt_idx<len(intervals)):
            if(start_time[strt_idx] >= end_time[end_idx]):
                used_rooms-=1
                end_idx+=1
            used_rooms += 1
            strt_idx+=1
        return used_rooms
            