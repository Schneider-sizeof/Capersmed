import os
import glob

files_to_update = [
    r"c:\Users\Athen\CAPERSMED\core\views.py",
    r"c:\Users\Athen\CAPERSMED\core\templates\base.html",
    r"c:\Users\Athen\CAPERSMED\core\templates\core\robots.txt",
    r"c:\Users\Athen\CAPERSMED\core\templates\core\product_detail.html",
    r"c:\Users\Athen\CAPERSMED\core\templates\core\products.html",
    r"c:\Users\Athen\CAPERSMED\core\templates\core\home.html",
    r"c:\Users\Athen\CAPERSMED\core\templates\core\blog_detail.html",
    r"c:\Users\Athen\CAPERSMED\core\context_processors.py"
]

for f in files_to_update:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        
        if "capersmed.pythonanywhere.com" in content:
            new_content = content.replace("capersmed.pythonanywhere.com", "www.capersmed.com")
            
            with open(f, "w", encoding="utf-8") as file:
                file.write(new_content)
            print(f"Updated {f}")
    except Exception as e:
        print(f"Error on {f}: {e}")
