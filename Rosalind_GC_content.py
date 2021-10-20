import re

with open("rosalind_gc (2).txt", "r") as f:
    contents = f.read()

ids = re.compile(r"(\bRosalind_\d{4})([^\>]+)")
matches = ids.finditer(contents)

keys = []
values = []
for match in matches:
    keys.append(match.group(1))
    values.append(match.group(2))

dictionary = dict(zip(keys, values))

list_of_percentages = []

def find_highest_GC():

    for key in dictionary:
        percentage = ((dictionary[key].count("G") + dictionary[key].count("C"))/(dictionary[key].count("G") + dictionary[key].count("C") + dictionary[key].count("A") + dictionary[key].count("T")) * 100)
        list_of_percentages.append(percentage)

find_highest_GC()

highest = max(list_of_percentages)

percentages_to_labels = dict(zip(list_of_percentages, keys))


def label_highest():
    for key in percentages_to_labels:
        if key == max(list_of_percentages):
            print(percentages_to_labels[key])
        else:
            pass
label_highest()

print(keys)
print(values)
print(list_of_percentages)
print(max(list_of_percentages))
