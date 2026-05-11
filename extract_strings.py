"""Extract all {% trans "..." %} strings from templates."""
import re, os

strings = set()
for root, dirs, files in os.walk('core/templates'):
    for fn in files:
        if fn.endswith('.html'):
            content = open(os.path.join(root, fn), encoding='utf-8').read()
            found = re.findall(r'\{%\s*trans\s+"([^"]+)"', content)
            strings.update(found)

for s in sorted(strings):
    print(s)

print(f"\n--- Total: {len(strings)} strings ---")
