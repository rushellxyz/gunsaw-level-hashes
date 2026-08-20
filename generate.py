import requests
import hashlib

print("Downloading...")
response = requests.get("https://github.com/jimmyking9999999/gunsaw-level-editor-plus/raw/refs/heads/main/Levels.json", timeout=5)
response.raise_for_status()
data = response.json()

print("Parsing...")
result = ""
for i in data["levels"]:
    checksum = hashlib.sha256(i["code"].encode('utf-8')).hexdigest()
    name = i["name"].replace(',', '.')
    result += (f'{checksum}, {name},')

print("Saving...")
with open("hashes.txt", "w") as f:
    f.write(result[:-1])
