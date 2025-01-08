sentence =input("Sentence: ")
sentence = sentence.replace(" ", "\n" "\a")  # "parse" sentence spaces with a new line
print(sentence, "\a")                   # Ring the bell :)
