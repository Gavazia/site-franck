import json
import re

in_file = r"C:\Users\Andy Gavaz\Documents\Antigravity\Personal_Tools\Site Franck\Asset\Scraped_Content\publications.md"
out_file = r"C:\Users\Andy Gavaz\Documents\Antigravity\Personal_Tools\Site Franck\Asset\Scraped_Content\publicaciones.json"

with open(in_file, "r", encoding="utf-8") as f:
    text = f.read()

entries = []

blocks = text.split('\n\n')
for block in blocks:
    # Look for lines starting with number
    match = re.search(r'^\d+\\?\.?\s+\((.*?)\)(.*?)$', block.strip(), flags=re.MULTILINE|re.DOTALL)
    if match:
        year = match.group(1).strip()
        rest = match.group(2).strip()
        
        title = ""
        journal = ""
        
        # Guilemets
        if '«' in rest and '»' in rest:
            parts = rest.split('»', 1)
            title = parts[0].split('«')[-1].strip()
            journal = parts[1].strip()
        # English quotes
        elif '“' in rest and '”' in rest:
            parts = rest.split('”', 1)
            title = parts[0].split('“')[-1].strip()
            journal = parts[1].strip()
        else:
            parts = rest.split(',', 1)
            title = parts[0].strip()
            journal = parts[1].strip() if len(parts) > 1 else ""
            
        # Clean up journal leading punctuation
        journal = journal.strip(', .')
        
        # Link check
        link = ""
        link_match = re.search(r'(http[s]?://[^\s)]+)', block)
        if link_match:
            link = link_match.group(1).strip()
            
        # Remove markdown link syntax in journal
        journal = re.sub(r'\[(.*?)\]\([^)]+\)', r'\1', journal)
        journal = re.sub(r'(http[s]?://[^\s]+)', '', journal).strip()
        
        entries.append({
            "titulo_articulo": title,
            "año": year,
            "revista_o_institucion": journal,
            "link_descarga": link
        })

with open(out_file, "w", encoding="utf-8") as f:
    json.dump({"publicaciones": entries}, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(entries)} publications to {out_file}")
