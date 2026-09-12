import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'class="group bg-background rounded-3xl border border-border\s+p-6 hover:-translate-y-2 hover:shadow-xl\s+transition-all duration-300"',
    'class="group bg-background rounded-3xl border border-border p-6 hover:-translate-y-2 hover:shadow-xl transition-all duration-300 flex flex-col h-full"',
    content
)

content = re.sub(
    r'<div class="mt-6 flex items-center gap-2 text-sm\s+font-bold text-accent">',
    '<div class="mt-auto pt-6 flex items-center gap-2 text-sm font-bold text-accent">',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)