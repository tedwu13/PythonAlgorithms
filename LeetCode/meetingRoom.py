
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
def canAttendMeetings(intervals):
        intervals.sort(key=lambda x: x.start)
    
        for i in xrange(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
    

    
print canAttendMeetings([[0,30],[5,10],[15, 16]])
                       
