"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

durations = dict()


def update_duration(duration_dict, number, dur):
    if duration_dict.get(number):
        duration_dict[number] = duration_dict[number] + dur
    else:
        duration_dict[number] = dur
    return duration_dict


assert update_duration({'x': 23}, 'x', 23) == {'x': 46}
assert update_duration({'x': 23}, 'y', 88) == {'x': 23, 'y': 88}

longest_duration = 0
telephone_number = ""

for call in calls:
    duration = int(call[3])

    caller = call[0]
    durations = update_duration(durations, caller, duration)
    if durations[caller] > longest_duration:
        longest_duration = durations[caller]
        telephone_number = caller

    callee = call[1]
    durations = update_duration(durations, callee, duration)
    if durations[callee] > longest_duration:
        longest_duration = durations[callee]
        telephone_number = callee

print('%s spent the longest time, %d seconds, on the phone during September 2016.' % (telephone_number,
                                                                                      longest_duration))

