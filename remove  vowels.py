def phrase(vowels):

    without_vowels = ""
    for letter in vowels:
        if letter in "AEIOUaeiou":
            without_vowels += ""
        else:
            without_vowels = without_vowels + letter

    return without_vowels

vowels = input("Enter a phrase: ")
without_vowels = phrase(vowels)
print (without_vowels)