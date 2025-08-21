filename = input("Enter file name: ")

with open(filename, 'r') as file:
    text = file.read()

words = text.split()
word_count = len(words)

freq_dict = {}
for word in words:
    word = word.lower()
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

most_frequent_word = max(freq_dict, key=freq_dict.get)
most_frequent_count = freq_dict[most_frequent_word]

print("Total words:", word_count)
print("Most frequent word:", most_frequent_word)
print("Occurrences:", most_frequent_count)
