# Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
# Output: 2
# Explanation:
# There is no meeting scheduled on the 4th and 8th days.

def countdays(days,meetings):
    events = []

    for start,end in meetings:
        events.append((start,1))
        events.append((end + 1, -1))
    events.sort()
    available_days, active_meetings, prev_day = 0,0,1
    for curr_day, change in events:
        if active_meetings == 0:
            available_days += (curr_day - prev_day)
        
        active_meetings += change
        prev_day = curr_day
    if active_meetings == 0:
        available_days += (days - prev_day + 1)
    
    return available_days

days = 10
meetings = [[1,10]]
print(countdays(days,meetings))  