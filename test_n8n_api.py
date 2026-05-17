import requests
import json

# Configuration
API_URL = "http://127.0.0.1:8000/api/v1/publish-blog/"
API_KEY = "n8n_secret_automation_key_2024"

# Mock data from n8n
payload = {
    "title_en": "Test Article: The Future of AI in Gastronomy",
    "title_fr": "Article de Test : L'avenir de l'IA en Gastronomie",
    "content_en": "## Introduction\nAI is revolutionizing how we source gourmet products...\n\n### Conclusion\nInnovation is key.",
    "content_fr": "## Introduction\nL'IA révolutionne la façon dont nous nous approvisionnons en produits gastronomiques...",
    "excerpt_en": "A deep dive into AI and food.",
    "category": "industry",
    "is_published": True,
    "author": "Automation Agent"
}

headers = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

print(f"🚀 Sending test payload to {API_URL}...")

try:
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print("✅ SUCCESS!")
        print(f"Response: {response.json()}")
        print(f"View article at: http://127.0.0.1:8000{response.json()['url']}")
    else:
        print(f"❌ FAILED (Status: {response.status_code})")
        print(f"Error: {response.text}")

except Exception as e:
    print(f"❌ CONNECTION ERROR: {e}")
