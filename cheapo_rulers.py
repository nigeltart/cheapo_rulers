# Convert arrays into sets so I can use 'in'
try recursion in version 2

# Find all possible markings


def all_possible_markings:
    max_size = 25


possible_markings[1] = [0, 1]
for current_size in range(2, max_size):
    for possible_marking in possible_markings[current_size - 1]:
        possible_markings[current_size] = possible_marking + current_size + [0, current_size]  # move this bit
return possible_markings


# Check whether each set of marks (possible_marking)can measure every length
def can_measure_all(marking):
    measurable_lengths = []


for start_mark in marking:
    for end_mark in marking:
        measured_length = end_mark - start_mark
        if measured_length not in measurable_lengths:
            add
            measured_length
            to
            measurable_lengths
            if len(measurable_length) == length_of_ruler + 1:  # including zero hence the +1
                return True  # can measure every length
return False


