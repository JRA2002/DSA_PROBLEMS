def clean_str(string):

    punctuation = [".",",","'","?","!"]
    new = ''

    for punct in string:
        if punct not in punctuation:
            new = new + punct
    return new

string = "Let's try, Mike..."
new = clean_str(string)

print(new)
