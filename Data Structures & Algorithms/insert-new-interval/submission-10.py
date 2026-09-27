class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        inserted_intervals = []
        inserted = False
        
        if not intervals:
            inserted_intervals = [newInterval]
        for start,end in intervals:
            if not inserted and start>newInterval[0]:
                inserted_intervals.append(newInterval)
                inserted=True
            inserted_intervals.append([start,end])
        if not inserted:
            inserted_intervals.append(newInterval)

        for start,end in inserted_intervals:
            if not result or result[-1][1] < start:
                result.append([start,end])
            else:
                result[-1][1] = max(end,result[-1][1])
        return result
        