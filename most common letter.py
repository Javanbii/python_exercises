string = "brocklphabet"
occurrence = {}
for character in string:
    if character in occurrence:
        occurrence[character] += 1
    else:
        occurrence[character] = 1
total_occurrence = max(occurrence, key = occurrence.get)
print(total_occurrence)