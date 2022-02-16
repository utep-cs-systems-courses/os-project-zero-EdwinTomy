"""
File that will count every word in a given file
"""
import sys  # arguments in the command-line
import os  # interacts with OS
import re  # regex

if len(sys.argv) != 3:
    print("Input three arguments!")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print("Input file doesn't exit: %s" % input_file)
    exit()

if not os.path.exists(output_file):
    print("Output file doesn't exit: %s" % output_file)
    exit()

word_count = {}

with open(input_file) as file:
    for line in file:
        lowercase_line = line.lower()
        words = re.findall(r'\w+', lowercase_line)
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

with open(output_file, "w") as file:
    for k, v in sorted(word_count.items(), key=lambda item: item[0]):
        file.write(k + " {}\n".format(v))

