# Vārdnīcu tīrītājs

# 3.a  Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val no kuras jāatbrīvojas kopā ar ar tās atslēgu.
# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
def clean_dict_value(d, bad_val):
    cleaned_dict = {}
    for key, value in d.items():
        if value != bad_val:
            cleaned_dict[key] = value
    return cleaned_dict

# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.
# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.
def clean_dict_values(d, v_list):
    cleaned_dict = {}
    for key, value in d.items():
        if value not in v_list:
            cleaned_dict[key] = value
    return cleaned_dict

