from collections import Counter

text = input("Enter a paragraph:\n")

sentences = text.split('.')

words = text.lower().split()
word_freq = Counter(words)

scores = {}

for sentence in sentences:
    score = 0
    for word in sentence.lower().split():
        score += word_freq[word]
    scores[sentence] = score

summary_sentences = sorted(
    scores,
    key=scores.get,
    reverse=True
)[:2]

summary = ". ".join(summary_sentences)

print("\n----- ORIGINAL TEXT -----")
print(text)

print("\n----- SUMMARY -----")
print(summary)
