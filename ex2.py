import re

_pattern = re.compile('''
^
(?P<ip>(\d{1,3}\.){3}\d{1,3})
[^[]+
\[(?P<date>[^]]+)\]
[^"]*
"((?P<method>\w+)\s+
  (?P<path>[^"]*)\s+HTTP/[^"]+)"
\s+
(?P<response>\d+)
''', re.VERBOSE)

for line in open('ex2.log', 'r', encoding='utf-8'):
    parsed = _pattern.search(line).groupdict()
    print('{ip:<15}: {path}'.format(**parsed))
