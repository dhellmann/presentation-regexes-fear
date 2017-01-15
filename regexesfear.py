import re
import sys

from output import capture

HIGHLIGHT = (
    '<span class="fragment highlight-yellow" '
    'data-fragment-index="1">'
    '{}'
    '</span>'
)


@capture
def showregex(s, p, flags=0):
    if flags & re.VERBOSE:
        print('\n<pre data-trim style="font-size: 80%">')
        print(p.replace('<', '&lt;'))
        print('</pre>')
    else:
        print('<h2><tt>{}</tt></h2>'.format(p))

    print('\n<pre data-trim data-noescape>')

    pat = re.compile(p, flags)

    if not pat.search(s):
        print('(no match)')
    else:
        prev = 0
        last = 0
        for m in pat.finditer(s):
            if prev < m.start():
                print(s[prev:m.start()], end='')
            prev = m.end()
            print(HIGHLIGHT.format(s[m.start():m.end()]), end='')
            last = m.end()
        if last:
            print(s[last:], end='')
        print()

        for i, m in enumerate(pat.finditer(s), 1):
            if m.groupdict():
                print('<span class="fragment fade-in" data-fragment-index="1">')
                for n, v in sorted(m.groupdict().items()):
                    print('{:<10s}: {}'.format(n, v))
                print('</span>')
            elif m.groups():
                print('<span class="fragment fade-in" data-fragment-index="1">')
                for j, g in enumerate(m.groups(), 1):
                    print('({}, {}) {}'.format(i, j, g))
                print('</span>')

    print('</pre>')
