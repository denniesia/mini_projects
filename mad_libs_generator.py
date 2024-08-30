with open('story.txt', 'r') as f: #open function, to open the file 'story.txt' in read mode 'r', 'w' is for write -> rewriting the file, 'f' is the context
    story = f.read() # gives the text

words = set()
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + r": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
