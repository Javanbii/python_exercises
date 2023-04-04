def phrase(number_vowels):
    count = 0
    for letter in number_vowels:
        if letter in "AEIOUaeiou":
            count += 1
    return count
number_vowels = input("Enter a phrase: ")
count = phrase(number_vowels)
print(count)