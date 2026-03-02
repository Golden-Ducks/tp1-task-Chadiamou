# line 10 (Task 1) & line 75 (Task 3)
using `.replace()` inside a loop is slow bcz it makes a new string every time
for punctuation, you can use a single loop or `str.translate`

# line 31 (Task 2)
`re.sub(r'\s+','', text)` will remove ALL spaces and merge everything into one giant word
you probably meant to use a single space `' '` as the replacement

# line 47 (Task 3)
naming your contraction dictionary `food_terms` is confusing bcz these aren't food lol
try using a name like `contractions_dict`

# line 65 (Task 3)
your contraction replacement happens AFTER you remove punctuation with `re.sub`
this means `"don't"` becomes `"dont"` first, so `.replace("don't", ...)` will never find a match
