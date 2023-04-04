word = input("Enter a word: ")
words = "".join(sorted(word .lower()))

word2 = input("Enter another word: ")
wordss = "".join(sorted(word2 .lower()))

if words == wordss:
    print(True)
else:
    print(False)