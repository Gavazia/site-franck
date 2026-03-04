import os
import re
import json
import urllib.request
import urllib.error

out_dir = r"C:\Users\Andy Gavaz\Documents\Antigravity\Personal_Tools\Site Franck\Asset\Scraped_Content"
assets = []

for file in os.listdir(out_dir):
    if file.endswith('.md'):
        path = os.path.join(out_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find markdown links or image tags: [text](link) or ![text](link)
            links = re.findall(r'\(?(https?://[^\s)]+)\)?', content)
            
            for link in links:
                link = link.strip().strip(')')
                if '.pdf' in link.lower() or '.jpg' in link.lower() or '.jpeg' in link.lower() or 'googleusercontent.com' in link.lower() or 'drive.google.com' in link.lower():
                    # check if the link is accessible
                    try:
                        req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                        response = urllib.request.urlopen(req, timeout=5)
                        status_code = response.getcode()
                        accessible = status_code == 200
                        message = f"Accessible (HTTP {status_code})"
                    except urllib.error.HTTPError as e:
                        accessible = False
                        message = f"HTTP Error {e.code}: Requires bypass"
                    except Exception as e:
                        accessible = False
                        message = f"Error connecting: {str(e)}"
                        
                    assets.append({
                        "source_file": file,
                        "asset_url": link,
                        "is_accessible": accessible,
                        "status_message": message
                    })

# deduplicate assets
unique_assets = {a["asset_url"]: a for a in assets}.values()

with open(os.path.join(out_dir, "asset_recovery.json"), "w", encoding="utf-8") as f:
    json.dump({"assets": list(unique_assets)}, f, indent=2, ensure_ascii=False)

print(f"Verified and extracted {len(unique_assets)} assets to asset_recovery.json")
