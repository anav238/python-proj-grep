import sys
import re

if len(sys.argv) < 3:
    raise ValueError("Wrong format! Correct format is: grep.py PATTERNS FILE [OPTION...]")

pattern = sys.argv[1]
filename = sys.argv[2]
options = sys.argv[3:]
pattern = pattern.replace("\"", "")
if '-v' in options:
    pattern = "(?!" + pattern + ")"

text_file = open(filename, 'r')
text = text_file.readlines()

matches = []
reg = re.compile(pattern)
for line in text:
    line = line.replace("\n", "")
    match = reg.match(line)
    if match is not None and (line == match.group() or '-v' in options):
        print(line)

text_file.close()
