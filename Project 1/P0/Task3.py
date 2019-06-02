"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def is_bangalore_number(number):
    return number.startswith('(080)')


def is_fixed_line(number):
    return number.startswith('(')


def is_mobile_number(number):
    return number.startswith('7') or number.startswith('8') or number.startswith('9')


def get_fixed_line_code(number):
    i = number.index(')')
    return number[1:i]


def get_mobile_prefix(number):
    return number[:4]


assert is_bangalore_number('(080)33251027')
assert is_fixed_line('(04344)649705')
assert is_mobile_number('90351 90193')
assert get_fixed_line_code('(04344)649705') == '04344'
assert get_mobile_prefix('90351 90193') == '9035'

codes = set()
number_of_calls = 0
number_of_calls_to_Bangalore = 0

for call in calls:
    caller = call[0]
    callee = call[1]
    if is_bangalore_number(caller):
        number_of_calls += 1
        if is_fixed_line(callee):
            codes.add(get_fixed_line_code(callee))
            if is_bangalore_number(callee):
                number_of_calls_to_Bangalore += 1
        elif is_mobile_number(callee):
            codes.add(get_mobile_prefix(callee))
        else:
            codes.add('140')

sorted_codes = sorted(codes)
percentage_of_calls_to_Bangalore = number_of_calls_to_Bangalore / number_of_calls * 100

print('The numbers called by people in Bangalore have codes:')
for code in sorted_codes:
    print(code)

print('%2.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.' %
      percentage_of_calls_to_Bangalore)
