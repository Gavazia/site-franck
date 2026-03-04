import json
import os
import re

out_dir = r"C:\Users\Andy Gavaz\Documents\Antigravity\Personal_Tools\Site Franck\Asset\Scraped_Content"
os.makedirs(out_dir, exist_ok=True)

files = [
    (r"C:\Users\Andy Gavaz\.gemini\antigravity\brain\c2cf4e3a-7a25-4112-9508-c5e131baffb7\.system_generated\steps\24\output.txt", "index.md", "https://sites.google.com/site/franckbietry"),
    (r"C:\Users\Andy Gavaz\.gemini\antigravity\brain\c2cf4e3a-7a25-4112-9508-c5e131baffb7\.system_generated\steps\25\output.txt", "carriere.md", "https://sites.google.com/site/franckbietry/carri%C3%A8re"),
    (r"C:\Users\Andy Gavaz\.gemini\antigravity\brain\c2cf4e3a-7a25-4112-9508-c5e131baffb7\.system_generated\steps\26\output.txt", "enseignements.md", "https://sites.google.com/site/franckbietry/enseignements-universitaires"),
    (r"C:\Users\Andy Gavaz\.gemini\antigravity\brain\c2cf4e3a-7a25-4112-9508-c5e131baffb7\.system_generated\steps\27\output.txt", "responsabilites.md", "https://sites.google.com/site/franckbietry/responsabilit%C3%A9s-acad%C3%A9miques"),
    (r"C:\Users\Andy Gavaz\.gemini\antigravity\brain\c2cf4e3a-7a25-4112-9508-c5e131baffb7\.system_generated\steps\28\output.txt", "publications.md", "https://sites.google.com/site/franckbietry/publications-scientifiques")
]

seo_migration = {}

for path, name, url in files:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        md = data.get("markdown", "")
        
        # Clean up Google Sites boilerplate
        md = re.sub(r"Search this site\n*Embedded Files\n*Skip to main content\n*Skip to navigation\n*", "", md)
        md = re.sub(r"\n*Google Sites\n*Report abuse\n*Back to site", "", md)
        md = re.sub(r"\n*Google Sites\n*Report abuse", "", md)
        
        # Clean heading links: ### [Copy heading link](...)
        md = re.sub(r"### \[Copy heading link\]\([^\)]+\)\s*", "### ", md)
        
        out_path = os.path.join(out_dir, name)
        with open(out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(md.strip())
            
        seo_migration[url] = name

with open(os.path.join(out_dir, "seo_migration.json"), "w", encoding='utf-8') as f:
    json.dump(seo_migration, f, indent=2, ensure_ascii=False)

print("Saved sanitized markdown files and seo_migration.json to " + out_dir)
