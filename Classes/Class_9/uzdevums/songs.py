# Definējiet klasi Song
# Klases construktora vajag būt trīs papildu 3 parametriem(self un vēl 3!)
# title pēc noklusējuma tukša string
# author pēc noklusējuma tukšs string
# lyrics pēc noklusējuma tukšs tuple
# konstruktors saglabātu šos trīs parametrus
# un papildu izdrukātu uz ekrāna "New Song made" - (pamēģiniet arī izdrukāt šeit author un title!)
# Uzrakstiet metodi sing kas izdrukā dziesmu pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Uzrakstiet metodi yell kas izdrukā dziesmu ar lieliem burtiem pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Bonuss: uztaisiet lai sing un yell varam izsaukt vairākas reizes (ķēdejot)
# Bonuss: uztaisiet papildu parametru max_lines, kas izdrukā tikai noteiktu rindiņu skaitu gan sing gan yell. Labāk taisiet ar kādu default vērtību piem. -1 , pie kuras tad izdrukā visas rindas.
# Par ķēdēšano bija šeit: https://www.das.lv/platforma/mod/page/view.php?id=690
# Izveidojiet vairākas dziesmas ar dziesmu tekstiem

# Piemērs:
# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
# ziemelmeita.sing(1).yell()
# Rezultāts uz ekrāna:
# Ziemeļmeita - Jumprava
# Gāju meklēt ziemeļmeitu
# Ziemeļmeita - Jumprava
# GĀJU MEKLĒT ZIEMEĻMEITU
# GARU, TĀLU CEĻU VEICU

# 1.B
# Tie kas jūtas komfortabli, uztaisiet Rap klasi kas manto no Song
# Papildu metode break_it ar diviem noklusētiem parametriem max_lines un drop vienādu ar "yeah", kura līdzīga sing, bet pievienot drop aiz katra vārda...
# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
# zrap.break_it(1, "yah")
# Ziemeļmeita - Jumprava
# Gāju YAH meklēt YAH ziemeļmeitu YAH

class Song:
    def __init__(self, title='', author='', lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print("New Song made")
        if self.title and self.author:
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")

    def sing(self, max_lines=-1):
        if self.title and self.author:
            print(f"{self.title} - {self.author}")
        if max_lines == -1:
            for line in self.lyrics:
                print(line)
        else:
            for line in self.lyrics[:max_lines]:
                print(line)

    def yell(self, max_lines=-1):
        if self.title and self.author:
            print(f"{self.title} - {self.author}")
        if max_lines == -1:
            for line in self.lyrics:
                print(line.upper())
        else:
            for line in self.lyrics[:max_lines]:
                print(line.upper())

class Rap(Song):
    def break_it(self, max_lines=-1, drop='yeah'):
        if self.title and self.author:
            print(f"{self.title} - {self.author}")
        if max_lines == -1:
            for line in self.lyrics:
                words = line.split()
                modified_line = ' '.join([word + ' ' + drop for word in words])
                print(modified_line)
        else:
            for line in self.lyrics[:max_lines]:
                words = line.split()
                modified_line = ' '.join([word + ' ' + drop for word in words])
                print(modified_line)

ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
zrap.break_it(1, "yah")
