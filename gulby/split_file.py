import sys
import math
import os

original_file_name = sys.argv[1]
split_count = int(sys.argv[2])

with open(original_file_name, 'r') as original_file:
    lines = list(original_file.readlines())

split_size = int(math.ceil(len(lines) / split_count))
split_lines = (lines[i:i+split_size] for i in range(0, len(lines), split_size))
for i, splits in enumerate(split_lines):
    split_file_name = '{}.{}'.format(original_file_name, i)
    with open(split_file_name, 'w') as split_file:
        split_file.writelines(splits)

print('complete')
