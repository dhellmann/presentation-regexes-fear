import contextlib
import functools
import io
import re
import sys

import cogapp


def capture(f):
    @functools.wraps(f)
    def wrap(*a, **kw):
        buf = io.StringIO()
        sys.stdout = buf
        f(*a, **kw)
        sys.stdout = sys.__stdout__
        results = buf.getvalue()
        sys.stderr.write(results)
        return results
    return wrap


@capture
def showregex(s, p):
    sys.stderr.write('\nshowregex({!r}, {!r})\n'.format(s, p))
    pat = re.compile(p)
    prev = -1
    last = 0
    for m in pat.finditer(s):
        if prev < m.start():
            print(s[prev+1:m.start()], end='')
        prev = m.start()
        print('<mark>{}</mark>'.format(s[m.start():m.end()]),
              end='')
        last = m.end()
    if last:
        print(s[last:], end='')
    print()
