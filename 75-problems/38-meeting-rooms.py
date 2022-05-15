def canAttendMeetings(intervals):
  if not intervals: return True
  intervals.sort(key=lambda a: a[0])
  for i in range(1, len(intervals)):
    i1 = intervals[i-1]
    i2 = intervals[i]

    if i2[0] < i1[1]:
      return False
  return True

print(canAttendMeetings([[0,4],[5,16],[15,20]]))
    