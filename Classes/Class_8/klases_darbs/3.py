# 3. Vai ir pangramma?
# uzrakstīt funkciju is_pangram, kas atgriež True, kad mytext parametrs satur visus burtus kas padoti a alfabetā.
# Savadāk atgriežam False.
# pangramma - teikums,vārdu virkne, kas satur visus alfabeta burtus - https://en.wikipedia.org/wiki/Pangram
# Atstarpes ignorējam,un uzskatam ka lielais burts ir tikpat derīgs kā mazais, t.i. šeit A un a -> a
# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     '''
#     '''
#     return None # here it should return True or False
# is_pangram("abcd foo") == False
# is_pangram("The quick brown fox jumps over the lazy dog") == True
# is_pangram("The five boxing wizards jump quickly") == True #ieverojam lielais T šeit
# PS. ar šo funkciju tad mēs varēsim pārbaudīt arī latviešu vai citu valodu pangramas, padodot a parametrā attiecīgā alfabēta burtus.

def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    mytext = mytext.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    for char in a:
        if char not in mytext:
            return False
    return True

print(is_pangram("abcd foo"))  # False
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("The five boxing wizards jump quickly"))  # True
print(is_pangram("Tā bija vasara, kad es biju mazs"))  # True
print(is_pangram("Tā bija vasara, kad es biju mazs", a='abcdefghijklmnopqrstuvwxyzāčēģīķļņšūž'))  # False
print(is_pangram("Tā bija vasara, kad es biju mazs", a='abcdefghijklmnopqrstuvwxyzāčēģīķļņšūžT'))  # True
