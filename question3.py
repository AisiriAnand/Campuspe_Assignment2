# ----------------------------------
# Question 3: String Manipulator
# ----------------------------------

try:
    sentence = input("Enter a sentence: ")

    # checking if input is empty
    if sentence.strip() == "":
        print("You entered an empty sentence.")
    else:
        print("\nOriginal:", sentence)

        # total characters including spaces
        print("Characters (with spaces):", len(sentence))

        # characters without spaces
        without_spaces = sentence.replace(" ", "")
        print("Characters (without spaces):", len(without_spaces))

        # total words
        words = sentence.split()
        print("Words:", len(words))

        # uppercase
        print("UPPERCASE:", sentence.upper())

        # lowercase
        print("lowercase:", sentence.lower())

        # title case
        print("Title Case:", sentence.title())

        # first and last word
        print("First word:", words[0])
        print("Last word:", words[-1])

        # reversed sentence
        reversed_sentence = sentence[::-1]
        print("Reversed:", reversed_sentence)

except Exception:
    print("Something went wrong. Please try again.")