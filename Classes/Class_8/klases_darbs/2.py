# 2. Kopējie Elementi
# Uzrakstiet funkciju,kas atgriež tuple ar kopējiem elementiem trijās virknēs. Virknes var būt list,tuple,string.
# get_common_elements(seq1,seq2,seq3)
# get_common_elements("abc",['a','b'],('b','c')) -> ('b',) # tuple are vienu element šim elementam seko komats
# # atceramies, ka mēs varam pārveidot virknes uz set ar set(virkne), un set uz tuple ar tuple(myset)
# PS Tiem, kas nav pirmo reizi ar pīpi uz jumta, padomāsim, vai varam uztaisīt funkciju, kas spēj apstrādat patvalīgu skaitu virkņu

def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    common_elements = set1.intersection(set2, set3)
    return tuple(common_elements)