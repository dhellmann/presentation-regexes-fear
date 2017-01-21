import cog
import subprocess

from output import capture


@capture
def showcode(filename, extras='data-trim data-noescape', lines=None):
    print('<pre><code {}>\n'.format(extras))
    with open(filename, 'r', encoding='utf-8') as f:
        body = f.readlines()
    if lines:
        # Editors start numbering lines at 1, so make it easier for me
        # to pass a start and stop pair by converting from the 1
        # indexed list to the 0 indexed list for the start value.
        body = body[lines[0] - 1:lines[1]]
    for line in body:
        print(line.replace('<', '&lt;'), end='')
    print('</code></pre>\n')


@capture
def runscript(filename, *args, extras='data-trim data-noescape', fade_in=False):
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
    print(output)
    print('\n</pre>\n')
