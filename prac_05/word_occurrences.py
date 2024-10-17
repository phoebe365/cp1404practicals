"""
Word Occurrences
Estimate: 30 minutes
Actual: 23 minutes
"""

def main():
    user_text = input("Enter a sentence: ")
    word_counts = count_words(user_text)
    max_word_len = max([len(word) for word in word_counts])

    print("\nWord counts:")
    for word in sorted(word_counts.keys()):  # Sorting keys (words) alphabetically
        print(f"{word:{max_word_len}}: {word_counts[word]}")

def count_words(text):
    text = text.lower()
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

main()