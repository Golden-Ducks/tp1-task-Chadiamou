import re

def normalize_numbers(text):
    number_words = {
          '0':'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        '10': 'ten'
    }
    for w, d in number_words.items():
        text = text.replace(w, d)
    return text

def normalize_text(text):
    food_terms = {
        "can't ": 'can not',
        "i'm": 'i am',
        "won't": 'will not',
        "don't": "do  not",
        "i'll": 'i will',
        "let's": 'let us',
        "that's": 'that is',
        "wasn't": 'was not',
        "couldn't": 'could not',
        "didn't": 'did not',
        "it't": 'it is',
        "he's": 'he is',
        "she's": 'she is',
        "frog's": 'frog it',
        "there's": 'there is',
        "we 're": 'we are'
    }
    for term, normalized in food_terms.items():
        text = text.replace(term, normalized)
    
    return text


with open("task2.txt", "r") as f:
    text = f.read()
text = text.lower()
text = re.sub(r"[^\w\s]", "", text)
text = re.sub(r"\s+", " ", text).strip()

text = normalize_numbers(text)
text = normalize_text(text)
punctuation = "!()-[]{};:,<>./?@#$%^&*_~'\""
for c in punctuation:
        b = text.replace(c, "")
text = b.split()
print(text)


