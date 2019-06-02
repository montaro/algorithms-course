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

longest_duration = 0
telephone_number = ""

for call in calls:
    duration = int(call[3])
    caller = call[0]
    if duration > longest_duration:
        longest_duration = duration
        telephone_number = caller

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

print("%s spent the longest time, %d seconds, on the phone during September 2016." % (telephone_number,
                                                                                      longest_duration))

