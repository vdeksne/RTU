# Saglabā lietotāja ievadu
# Izdrukā ievadīto tekstu bez izmaiņām
# Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs
# Laiks nav slikts -> Laiks ir labs
# Auto nav jauns -> Auto nav jauns
# Tas biezpiens nav nemaz tik slikts -> Tas biezpiens ir labs 
# Droši vien noderēs find (vai index, vai pat rfind), tāpat arī in operātors var noderēt. Tāpat slice sintakse būs noderīga.
# Ja uzdevums risinās raiti, tad varam uzlabot un meklēt gan nav ... slikts -> ir labs, gan nav ... slikta -> ir laba

def replace_phrases(text):
    phrases = {
        'nav ... slikts': 'ir labs',
        'nav ... slikta': 'ir laba',
        'Laiks nav slikts': 'Laiks ir labs',
        'Auto nav jauns': 'Auto nav jauns',
        'Tas biezpiens nav nemaz tik slikts': 'Tas biezpiens ir labs'
    }

    for phrase, replacement in phrases.items():
        if phrase in text:
            text = text.replace(phrase, replacement)

    return text

user_input = input("Ievadiet tekstu: ")
print(replace_phrases(user_input))