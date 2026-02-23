# ----------------------------------
# Question 17: Palindrome Checker
# ----------------------------------

text = input("Enter word/number: ")

original = text
processed = text.lower()

reversed_text = processed[::-1]

print("Original:", original)
print("Reversed:", reversed_text)

if processed == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")