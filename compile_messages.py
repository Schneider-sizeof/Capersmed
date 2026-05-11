"""Compile .po files to .mo without requiring GNU gettext."""
import os
import struct

def compile_po_to_mo(po_path, mo_path):
    """Simple .po to .mo compiler."""
    messages = []
    current_msgid = None
    current_msgstr = None
    in_msgid = False
    in_msgstr = False
    
    with open(po_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('msgid "'):
                if current_msgid is not None and current_msgid != '':
                    messages.append((current_msgid, current_msgstr or ''))
                content = line[7:-1]
                current_msgid = content
                current_msgstr = None
                in_msgid = True
                in_msgstr = False
            elif line.startswith('msgstr "'):
                content = line[8:-1]
                current_msgstr = content
                in_msgid = False
                in_msgstr = True
            elif line.startswith('"') and line.endswith('"'):
                content = line[1:-1]
                if in_msgid:
                    current_msgid += content
                elif in_msgstr:
                    current_msgstr = (current_msgstr or '') + content
            elif line == '' or line.startswith('#'):
                in_msgid = False
                in_msgstr = False
        
        # Don't forget the last entry
        if current_msgid is not None and current_msgid != '':
            messages.append((current_msgid, current_msgstr or ''))
    
    # Sort by msgid (required by .mo format)
    messages.sort(key=lambda x: x[0].encode('utf-8'))
    
    # Build .mo file
    # .mo format: https://www.gnu.org/software/gettext/manual/html_node/MO-Files.html
    n = len(messages)
    
    # Header
    keystart = 28 + 8 * n * 2
    valuestart = keystart
    
    # Calculate offsets
    keys = []
    values = []
    for msgid, msgstr in messages:
        keys.append(msgid.encode('utf-8'))
        values.append(msgstr.encode('utf-8'))
    
    # Key offsets
    key_offsets = []
    offset = keystart + sum(len(k) + 1 for k in keys)  # +1 for null terminator
    
    # Recalculate: keys start after the offset tables
    key_start_offset = 28 + 8 * n * 2
    val_start_offset = key_start_offset
    
    # First pass: compute key area
    ko = key_start_offset
    key_entries = []
    for k in keys:
        key_entries.append((len(k), ko))
        ko += len(k) + 1  # null terminator
    
    # Values start after all keys
    vo = ko
    val_entries = []
    for v in values:
        val_entries.append((len(v), vo))
        vo += len(v) + 1
    
    # Write the file
    output = []
    # Magic number
    output.append(struct.pack('I', 0x950412de))
    # Revision
    output.append(struct.pack('I', 0))
    # Number of strings
    output.append(struct.pack('I', n))
    # Offset of original strings table
    output.append(struct.pack('I', 28))
    # Offset of translated strings table
    output.append(struct.pack('I', 28 + 8 * n))
    # Size of hashing table (0 = no hash)
    output.append(struct.pack('I', 0))
    # Offset of hashing table
    output.append(struct.pack('I', 0))
    
    # Original strings table
    for length, offset in key_entries:
        output.append(struct.pack('II', length, offset))
    
    # Translated strings table
    for length, offset in val_entries:
        output.append(struct.pack('II', length, offset))
    
    # Key strings
    for k in keys:
        output.append(k + b'\x00')
    
    # Value strings
    for v in values:
        output.append(v + b'\x00')
    
    with open(mo_path, 'wb') as f:
        f.write(b''.join(output))


if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(base, 'locale')
    
    for lang in os.listdir(locale_dir):
        po_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.po')
        mo_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.mo')
        if os.path.isfile(po_path):
            compile_po_to_mo(po_path, mo_path)
            print(f'Compiled: {lang}/LC_MESSAGES/django.mo')
    
    print('Done!')
