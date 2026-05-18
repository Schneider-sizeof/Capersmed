import os
import django
import time
from deep_translator import GoogleTranslator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capersmed.settings')
django.setup()

from core.models import Certification

LANGS = ['ar', 'fr', 'es', 'it', 'pt']

print("Starting Certification DB Translation...")

certs = Certification.objects.all()

for cert in certs:
    print(f"\nProcessing Certification: {cert.name}")
    updated = False
    
    for lang in LANGS:
        translator = GoogleTranslator(source='en', target=lang)
        
        # Check and translate subtitle
        subtitle_field = f'subtitle_{lang}'
        subtitle_en = getattr(cert, 'subtitle_en', '')
        subtitle_val = getattr(cert, subtitle_field, '')
        
        if subtitle_en and not subtitle_val:
            try:
                translated_sub = translator.translate(subtitle_en)
                setattr(cert, subtitle_field, translated_sub)
                print(f"  - Translated subtitle to {lang.upper()}")
                updated = True
                time.sleep(0.1)
            except Exception as e:
                print(f"  - Failed subtitle {lang}: {e}")
                
        # Check and translate description
        desc_field = f'description_{lang}'
        desc_en = getattr(cert, 'description_en', '')
        desc_val = getattr(cert, desc_field, '')
        
        if desc_en and not desc_val:
            try:
                translated_desc = translator.translate(desc_en)
                setattr(cert, desc_field, translated_desc)
                print(f"  - Translated description to {lang.upper()}")
                updated = True
                time.sleep(0.1)
            except Exception as e:
                print(f"  - Failed description {lang}: {e}")

    if updated:
        cert.save()
        print(f"Saved updates for {cert.name}")

print("\nDone! Database certifications translated.")
