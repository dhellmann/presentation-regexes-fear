import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**.  This **too**.'
html = bold.sub(r'<b>\1</b>', text)

print('Text:', text)
print('HTML:', html)
