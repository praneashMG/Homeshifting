import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the flex row container
content = content.replace(
    '''<div class="flex flex-col lg:flex-row lg:items-end
                    justify-between gap-6 mb-12 lg:mb-14">''',
    '''<div class="flex flex-col items-center text-center gap-6 mb-12 lg:mb-14">'''
)

# And add mx-auto to the max-w-3xl div to center it properly, and remove it being left aligned.
content = content.replace(
    '''<div class="max-w-3xl">''',
    '''<div class="max-w-3xl mx-auto flex flex-col items-center">'''
)

# the paragraph max-w-2xl should also be centered
content = content.replace(
    '''<p class="mt-4 text-base sm:text-lg
                          text-secondary-text leading-7 max-w-2xl">''',
    '''<p class="mt-4 text-base sm:text-lg
                          text-secondary-text leading-7 max-w-2xl mx-auto">'''
)

# For the small trust indicator, we'll keep it as inline-flex and center it or remove hidden lg:flex
content = content.replace(
    '''<!-- Small trust indicator -->
            <div class="hidden lg:flex items-center gap-3
                        px-5 py-3 rounded-2xl
                        border border-border bg-hover">''',
    '''<!-- Small trust indicator -->
            <div class="inline-flex items-center gap-3
                        px-5 py-3 rounded-2xl
                        border border-border bg-hover mt-2">'''
)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)