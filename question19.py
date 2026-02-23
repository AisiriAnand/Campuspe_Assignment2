# # ----------------------------------
# Question 19: Text Analysis
# ----------------------------------

# Function to count words
def count_words(text):
    words = text.split()
    return len(words)

# Function to count vowels
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

# Function to count consonants
def count_consonants(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

# Reverse text
def reverse_text(text):
    return text[::-1]

# Check palindrome
def is_palindrome(text):
    processed = text.lower().replace(" ", "")
    return processed == processed[::-1]

# Remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

# Word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# Longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Main analysis function
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    long_word = longest_word(text)
    print("Longest word:", long_word, "(", len(long_word), "letters )")

    print("Word Frequency:")
    freq = word_frequency(text)
    for key in freq:
        print(key + ":", freq[key])

# Taking input
user_text = input("Enter text: ")
analyze_text(user_text)