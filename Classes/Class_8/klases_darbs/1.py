# 1. Min, Avg, Max
# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, aritmētisko vidējo un lielāko vērtību no virknes.
# get_min_avg_max([0,10,1,9]) -> (0,5,10)
# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 
# 1b tiem, kas pieredzējušāki
# Uzrakstiet funkciju get_min_med_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, medianu un lielāko vērtību no virknes.
# Median vērtība ir vērtiba, kas sakartotā virknē ir paša vidū. Ja virknes skaits ir pāra tad vidū ir divas vērtības.
# No vidus vērtībām tad ņem vidējo.
# get_min_med_max([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max("baaac") -> ('a','a','c')
#  # ar string var būt interesanti rezultāti pie pāra skaita ņemot vidējo, tāpēc labak dot abus vidējos
# get_min_med_max("faaacb") -> ('a', 'ab', 'f') 
# ienākošā sequence var būt tuple vai list ar vienāda tipa vērtībām, vai pat string.

def get_min_avg_max(sequence):
    sequence = sorted(sequence)
    minimum = sequence[0]
    maximum = sequence[-1]
    average = sum(sequence) / len(sequence)
    return minimum, average, maximum

def get_min_med_max(sequence):
    sequence = sorted(sequence)
    minimum = sequence[0]
    maximum = sequence[-1]
    median = sequence[len(sequence)//2] if len(sequence) % 2 != 0 else (sequence[len(sequence)//2 - 1] + sequence[len(sequence)//2]) / 2
    return minimum, median, maximum

# Example usage
sequence = [0, 10, 1, 9]
result = get_min_avg_max(sequence)
print(result)  # Output: (0, 5.0, 10)

sequence = [1, 5, 8, 4, 3]
result = get_min_med_max(sequence)
print(result)  # Output: (1, 4, 8)

sequence = [2, 2, 9, 9, 4, 3]
result = get_min_med_max(sequence)
print(result)  # Output: (2, 3.5, 9)

sequence = "baaac"
result = get_min_med_max(sequence)
print(result)  # Output: ('a', 'a', 'c')

sequence = "faaacb"
result = get_min_med_max(sequence)
print(result)  # Output: ('a', 'ab', 'f')
