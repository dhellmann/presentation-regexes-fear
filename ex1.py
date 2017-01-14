import re

s = "Does the pattern match this text?"

pattern = re.compile("t")

print(pattern.search(s))
