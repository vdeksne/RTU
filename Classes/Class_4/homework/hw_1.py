# # Strings - Klases Uzdevumi
# Juceklis
# Lietotājs ievada vārdu.
# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
# Valdis -> Sidlav, pamatigs juceklis vai ne V?
# Juceklis
name = input("Enter your name: ")
reversed_name = name[::-1].capitalize()
message = f"{reversed_name}, pamatigs juceklis vai ne {name[0]}?"
print(message)

# Teksta simbola atpazīšana
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

# Teksta pārveidošana
input_text = input("Enter the text: ")
if "nav ... slikts" in input_text:
    output_text = input_text.replace("nav ... slikts", "ir labs")
else:
    output_text = input_text
print(output_text)

# Uzrakstīt programmu teksta atpazīšanai karātavu spēlei
# Lietotājs(pirmais spēlētājs) ievada tekstu.
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# Kartupeļu lauks -> ********* *****
# ievada a -> *a****** *a***
# Principā tas ir labs iesākums karātavu spēlei.


# Saglabā lietotāja ievadu
# Izdrukā ievadīto tekstu bez izmaiņām
# Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs
# Laiks nav slikts -> Laiks ir labs
# Auto nav jauns -> Auto nav jauns
# Tas biezpiens nav nemaz tik slikts -> Tas biezpiens ir labs 
# Droši vien noderēs find (vai index, vai pat rfind), tāpat arī in operātors var noderēt. Tāpat slice sintakse būs noderīga.
# Ja uzdevums risinās raiti, tad varam uzlabot un meklēt gan nav ... slikts -> ir labs, gan nav ... slikta -> ir laba