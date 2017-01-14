import re
import sys

from output import capture


@capture
def showregex(s, p):
    print('<pre data-trim class="fragment fade-in">')
    pat = re.compile(p)
    prev = -1
    last = 0
    for m in pat.finditer(s):
        if prev < m.start():
            print(s[prev+1:m.start()], end='')
        prev = m.start()
        print('<mark>{}</mark>'.format(s[m.start():m.end()]), end='')
        last = m.end()
    if last:
        print(s[last:], end='')
    print('</pre>')
