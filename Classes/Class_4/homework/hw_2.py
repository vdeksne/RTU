# Uzrakstīt programmu teksta atpazīšanai karātavu spēlei
# Lietotājs(pirmais spēlētājs) ievada tekstu.
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# Kartupeļu lauks -> ********* *****
# ievada a -> *a****** *a***
# Principā tas ir labs iesākums karātavu spēlei.

text = input("Enter the text: ")
hidden_text = '*' * len(text)
print(hidden_text)

guess = input("Enter a character: ")
if guess in text:
    revealed_text = ''
    for char in text:
        if char == guess:
            revealed_text += char
        else:
            revealed_text += '*'
    print(revealed_text)
else:
    print("Character not found in the text")
