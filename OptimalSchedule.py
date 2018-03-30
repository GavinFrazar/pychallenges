def timeToMinutes(t):
    afternoon = False
    if (t.endswith("pm")):
        afternoon = True
    t = t.strip("am")
    t = t.strip("pm")
    hour, minute = t.split(":")
    hour = int(hour)
    minute = int(minute)
    if (afternoon):
        if (hour < 12):
            hour = hour + 12
    else:
        if (hour == 12):
            hour = hour - 12
    t = hour*60 + minute
    return t

def main():
    #start_time,duration
    input = ["05:00am,60", "10:00am,30", "10:15am,45", "11:00am,20", "11:15am,60", "12:30pm,60", "01:00pm,75"]

    # Not busy from 08:00 to 18:00 (8am - 6pm)
    busy = [True if (k < 8*60 or k > 18*60) else False for k in range(0, 24*60)]
    
    # Convert the input's start_time into minutes
    simplified_input = []
    for req in input:
        t, dur = req.split(",")
        dur = int(dur)
        t = timeToMinutes(t)
        simplified_input.append([t,dur])

    # Sort the input in descending order of duration (this makes the whole algo nlogn btw)
    simplified_input.sort(key=lambda x: x[1], reverse=True)

    max_dur = 0
    for req in simplified_input:
        start_time = req[0]
        end_time = req[0] + req[1]
        if (not (busy[start_time] or busy[end_time])):
            # Add the request to the schedule, and add 5 minutes for a break afterward, UNLESS the appointment ends at or after 17:55 == 17*60 + 55 minutes
            break_time = 5
            if (end_time >= 17*60 + 55):
                break_time = 0
            
            # Mark the schedule busy for the newly accepted appointment + the break time afterward
            for k in range(start_time, end_time + break_time + 1):
                busy[k] = True
            
            # Update the max duration that the doc will work today
            max_dur = max_dur + (end_time - start_time)
    print(max_dur)

main()