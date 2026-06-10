from collections import Counter

# Get input text from user
text = input("Enter a paragraph:\n")

# Split text into sentences
sentences = text.split('.')

# Count word frequencies
words = text.lower().split()
word_freq = Counter(words)

# Score each sentence
scores = {}

for sentence in sentences:
    score = 0
    for word in sentence.lower().split():
        score += word_freq[word]
    scores[sentence] = score

# Select top 2 important sentences
summary_sentences = sorted(
    scores,
    key=scores.get,
    reverse=True
)[:2]

# Generate summary
summary = ". ".join(summary_sentences)

# Display results
print("\n----- ORIGINAL TEXT -----")
print(text)

print("\n----- SUMMARY -----")
print(summary)
