from collections import Counter
import re

def analyze_word_frequency(text):
    # Remove punctuation and make lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# Example 1
text1 = "Hello world! Hello AI."
freq1 = analyze_word_frequency(text1)
print("Example 1:", freq1)

# Example 2
text2 = "Python is great. Python is easy to learn."
freq2 = analyze_word_frequency(text2)
print("Example 2:", freq2)

# Example 3
text3 = "Data science, machine learning, and AI are related fields."
freq3 = analyze_word_frequency(text3)
print("Example 3:", freq3)