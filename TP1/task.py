def fct(b):
    number_words = {
        '0':'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        '10': 'ten'
    }
    for k, d in number_words.items():
        b = b.replace(k, d) 
    punctuation = "!()-[]{};:,<>./?@#$%^&*_~'\""
    for c in punctuation:
        b = b.replace(c, "")
    words = b.split()
    return words
sentences = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
sentences2 = "Handling Contractions Isn't Hard."
sentences3 = "We only had 8 chamiyya, no pizza, and one tea."
sentences4 = "Is 6 too much? I ate nine bourak lol."
lowercased_sentences = sentences.lower()
lowercased_sentences2 = sentences2.lower()
lowercased_sentences3 = sentences3.lower()
lowercased_sentences4 = sentences4.lower()

a = fct(lowercased_sentences)
b = fct(lowercased_sentences2)
c = fct(lowercased_sentences3)
d = fct(lowercased_sentences4)
print(a,'\n',b,'\n',c,'\n',d)

