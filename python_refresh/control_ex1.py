def smallest_positive(in_list):
    smallest_pos = None
    for item in in_list:
        if item > 0:
            if smallest_pos is None or item < smallest_pos:
                smallest_pos = item
    return smallest_pos

print(smallest_positive([4, -6, 7, 2, -4, 10]))
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
print(smallest_positive([-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58]))
print(smallest_positive([-3.53, -56.3, 11.17, -25.21, 96.21, -44.62, 94.95, 65.85, 26.79, -88.16]))
print(smallest_positive([-46.41, -55.11, 40.64]))
print(smallest_positive([-98.35]))
print(smallest_positive([-1, -2]))
