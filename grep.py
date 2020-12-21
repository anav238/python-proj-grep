import sys
import re

if len(sys.argv) < 3:
    raise ValueError("Wrong format! Correct format is: grep.py [OPTION...] PATTERNS FILE")

pattern = sys.argv[1]
filename = sys.argv[2]
pattern = pattern.replace("\"", "")

text_file = open(filename, 'r')
text = text_file.readlines()

matches = []
reg = re.compile(pattern)
for line in text:
    line = line.replace("\n", "")
    match = reg.match(line)
    if match is not None and line == match.group():
        print(line)

text_file.close()
