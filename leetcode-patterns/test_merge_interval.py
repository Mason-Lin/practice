# take a look merge-interval.jpg
def compare_intervals(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if end1 < start2:
        return "Case 1: Interval1 is completely before Interval2"
    if start1 > end2:
        return "Case 2: Interval1 is completely after Interval2"
    if start2 <= start1 and end1 <= end2:
        return "Case 3: Interval1 is completely inside Interval2"
    if start1 <= start2 and end2 <= end1:
        return "Case 4: Interval2 is completely inside Interval1"
    if start2 <= end1 <= end2:
        return "Case 5: Interval1 is partially overlapping Interval2 from the left"
    if start1 <= end2 <= end1:
        return "Case 6: Interval1 is partially overlapping Interval2 from the right"
    return "Intervals have some other relation"


intervals = [[1, 2], [2, 4], [4, 5], [5, 7], [7, 8], [2, 7]]
second_interval = [3, 6]
for interval in intervals:
    result = compare_intervals(interval, second_interval)
    print(interval, second_interval, result)
