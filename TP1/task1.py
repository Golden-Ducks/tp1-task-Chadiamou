import re
with open("task1.txt", "r") as f:
    text = f.read()
text = text.lower()
text = re.sub(r'\d+', '', text)
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+','', text)
text = re.sub(r"[–]", "", text)
punctuation = "!()-[]{};:,<>./?@#$%^&*_~'\""
for c in punctuation:
        text = text.replace(c, "")

words = text.split()
print(text)