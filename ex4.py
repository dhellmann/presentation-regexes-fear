import re

with open('ex4.txt', 'r', encoding='utf-8') as f:
    text = f.read()

func = re.compile(
    r'''
    :func:
    `
    ([^()]+?)
    (?:\(\))?
    `
    ''',
    flags=re.VERBOSE | re.MULTILINE,
)
text = func.sub(r'``\1()``', text)

strip = re.compile(
    r'''
    :(?:class|data|const|command):
    `
    ([^()]+?)
    (?:\(\))?
    `
    ''',
    flags=re.VERBOSE | re.MULTILINE,
)
text = strip.sub(r'``\1``', text)

print(text)
