import cog
import subprocess

from tools.output import capture


@capture
def showfile(filename, extras='data-trim data-noescape', lines=None, mark=()):
    print('<pre class="lineselect_selectable" {}>'.format(extras))
    with open(filename, 'r', encoding='utf-8') as f:
        body = f.readlines()
    if lines:
        # Editors start numbering lines at 1, so make it easier for me
        # to pass a start and stop pair by converting from the 1
        # indexed list to the 0 indexed list for the start value.
        body = body[lines[0] - 1:lines[1]]
    for i, line in enumerate(body, 1):
        out = line.replace('<', '&lt;')
        out = '<span class="line">{}</span>'.format(out)
        if i in mark:
            out = '<mark>{}</mark>'.format(out)
        print(out, end='')
    print('</pre>\n')


@capture
def showcode(filename, extras='data-trim data-noescape', lines=None, mark=()):
    print('<pre><code class="lineselect_selectable" {}>'.format(extras))
    with open(filename, 'r', encoding='utf-8') as f:
        body = f.readlines()
    if lines:
        # Editors start numbering lines at 1, so make it easier for me
        # to pass a start and stop pair by converting from the 1
        # indexed list to the 0 indexed list for the start value.
        body = body[lines[0] - 1:lines[1]]
    for i, line in enumerate(body, 1):
        out = line.replace('<', '&lt;')
        if i in mark:
            out = '<mark>{}</mark>'.format(out)
        print(out, end='')
    print('</code></pre>\n')


@capture
def runscript(filename, *args, extras='data-trim data-noescape', fade_in=False, mark=()):
    print('<pre {}'.format(extras), end='')
    if fade_in:
        print(' class="fragment fade-in"', end='')
    print('>')
    result = subprocess.run(
        ['python3', filename] + list(args),
        stdout=subprocess.PIPE,
    )
    output = result.stdout.decode('utf-8').rstrip('\n')
    output = output.replace('<', '&lt;')
    for i, line in enumerate(output.splitlines(), 1):
        if i in mark:
            line = '<mark>{}</mark>'.format(line)
        print(line)
    print('\n</pre>\n')
