sentence = input("Sentence: ")
query = input("Word to look for in sentence: ")

# sanitize our inputs
sentence = sentence.lower().strip()
print("Sentence Sanitized: ", sentence)
num_occurrences = sentence.count(query)
print(f"There are {num_occurrences} instances of '{query}' in the sentence.")
