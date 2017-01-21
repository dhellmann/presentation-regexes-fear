import cog
import subprocess

from output import capture


@capture
def showcode(filename, extras='data-trim data-noescape'):
    print('<pre><code {}>\n'.format(extras))
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
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
    print(result.stdout.decode('utf-8').rstrip('\n'))
    print('\n</pre>\n')
