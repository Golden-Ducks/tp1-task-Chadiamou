import nltk

from nltk.tokenize import word_tokenize
import string
import spacy
import contractions 

def text_cleaning(b):
    b = contractions.fix( b ) #fixe le text
    punctuation ="!()-[]{};:,<>./?@#$%^&*_~'\""
    cleaned_txt = ''
    for char in b:
        if char not in punctuation:
            cleaned_txt =cleaned_txt + char
    cleaned_txt = spacy_fct(cleaned_txt)          #spacy
    return cleaned_txt

def spacy_fct(cleaned_txt):
 nlp = spacy.load("en_core_web_sm")
 text_sp = nlp(cleaned_txt)

 cleaned_txt=[t for t in text_sp if not t.is_stop ]
 return cleaned_txt

def text_tokenization(text):
  text= str(text)
  tokens = word_tokenize(text)
  tokens_clean = [w for w in tokens if w not in string.punctuation]
  return tokens_clean
   

def text_normalization(r):
    normalized_r = []
    for word in r:
        normalized_r.append(word.lower())
    
    return normalized_r

def build_vocabulary(all_tokens):
    return list(set(all_tokens))   #sup les doublons

def document_to_vector(document, vocab):

    vector = []
    for word in vocab:
        vector.append(1 if word in document else 0)
    return tuple(vector)

# Original documents
D1 = "I feel good."
D2 = "I do feel even better now, thank you!"
D3 = "I feel bad"
D1 =D1.lower()
D2 =D2.lower()
D3 =D3.lower()

#  1: Text cleaning
D1_clean = text_cleaning(D1)  
D2_clean = text_cleaning(D2)  
D3_clean = text_cleaning(D3)  

print("After Text Cleaning:")
print(f"D1: '{D1_clean}'")
print(f"D2: '{D2_clean}'")
print(f"D3: '{D3_clean}'")

# 2: Text tokenization
D1_tokens = text_tokenization(D1_clean)
D2_tokens = text_tokenization(D2_clean)
D3_tokens = text_tokenization(D3_clean)

print("\nAfter Text Tokenization:")
print(f"D1: {D1_tokens}")
print(f"D2: {D2_tokens}")
print(f"D3: {D3_tokens}")

#  3: Text normalization
D1_normalized = text_normalization(D1_tokens)
D2_normalized = text_normalization(D2_tokens)
D3_normalized = text_normalization(D3_tokens)

print("\nAfter Text Normalization (Lowercase):")
print(f"D1: {D1_normalized}")
print(f"D2: {D2_normalized}")
print(f"D3: {D3_normalized}")

#pour faire sa vocabulary vector = (feel, good, better, thank, happened, bad)
all_tokens = D1_normalized + D2_normalized + D3_normalized
vocabulary = build_vocabulary(all_tokens)
vocabulary.sort()  

print(f"\nVocabulary: {vocabulary}")

# la derniere etap
D1_vector = document_to_vector(D1_normalized, vocabulary)
D2_vector = document_to_vector(D2_normalized, vocabulary)
D3_vector = document_to_vector(D3_normalized, vocabulary)

print("\nFinal Bag of Words Vectors:")
print(f"D1 : {D1_vector}")
print(f"D2 : {D2_vector}")
print(f"D3 : {D3_vector}")
