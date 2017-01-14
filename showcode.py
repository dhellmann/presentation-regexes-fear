import cog
import subprocess


def showcode(filename, extras='data-trim'):
    cog.out('<pre><code {}>\n'.format(extras))
    with open(filename, 'r', encoding='utf-8') as f:
        cog.out(f.read())
    cog.out('</code></pre>\n')


def runscript(filename, extras='data-trim', fade_in=False):
    cog.out('<pre {}'.format(extras))
    if fade_in:
        cog.out(' class="fragment fade-in"')
    cog.out('>\n')
    result = subprocess.run(
        ['python3', filename],
        stdout=subprocess.PIPE,
    )
    cog.out(result.stdout.decode('utf-8'))
    cog.out('</pre>\n')
