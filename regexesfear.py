import re
import sys

from output import capture


@capture
def showregex(s, p):
    print('<pre data-trim>')
    print('{}\n\n{}'.format(s, p))
    print('</pre>\n')
    print('<pre data-trim class="fragment fade-in">')

    pat = re.compile(p)

    if not pat.search(s):
        print('(no match)')
    else:
        prev = 0
        last = 0
        for m in pat.finditer(s):
            if prev < m.start():
                print(s[prev:m.start()], end='')
            prev = m.end()
            print('<mark>{}</mark>'.format(s[m.start():m.end()]), end='')
            last = m.end()
        if last:
            print(s[last:], end='')
        print()

        # Show the numbers of each match.
        # prev = 0
        # last = 0
        # for i, m in enumerate(pat.finditer(s), 1):
        #     # print(last, prev, m.start(), m.end())
        #     print(' ' * last, end='')
        #     if prev < m.start():
        #         print(' ' * (m.start() - prev), end='')
        #     prev = m.end()
        #     for j in range(m.end() - m.start()):
        #         print(i, end='')
        #     print()
        #     last = m.end()

        # Show the indexes of each match.
        # prev = 0
        # for i, l in enumerate(s):
        #     print('{:02d}'.format(i), l)
        # for m in pat.finditer(s):
        #     print(prev)
        #     if prev < m.start():
        #         print('P {:02d} {:02d} {}'.format(prev, m.start(), s[prev:m.start()]))
        #     prev = m.end()
        #     print('M {:02d} {:02d} {}'.format(m.start(), m.end(), s[m.start():m.end()]))

    print('</pre>')
